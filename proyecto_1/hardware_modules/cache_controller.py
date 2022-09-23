from sys import path
path.append("../")
from constants import *
from common import *

from cache_L1 import Cache

class CacheController:

    ########## Device creation ##########
    def __init__(self, number):
        self.name = "Cache_controller" + str(number)
        self.processor_ID = number
        self.cache = Cache()
        self.bus = None
        self.last_accessed_blocks = [i for i in range(CACHE_BLOCKS)]
        log(self.name, "created")

    def connect_bus(self, bus):
        self.bus = bus
        log(self.name, "connected to bus")

    ########## Communication ##########
    def issue_mem_read(self, instruction):
        data = self.bus.transmit_instruction(instruction)
        return data

    def issue_mem_write(self, instruction):
        self.bus.transmit_instruction(instruction)

    def broadcast(self, instruction):
        log(self.name, "broadcasting " + str(instruction))
        data = self.bus.propagate_broadcast(instruction)
        return data

    ########## Cache control ##########

    def cache_new_data(self, status, data):
        least_used_key = self.last_accessed_blocks[-1]
        log(self.name, 'caching new block ' + str(least_used_key) + str({'status': status, 'data': data}))
        self.cache.write_block(least_used_key, {'status': status, 'data': data})
        self.update_access(least_used_key)

    def write_to_cache_block(self, block_key, status, data):
        log(self.name, 'writing to cache block ' + str(block_key) + str({'status': status, 'data': data}))
        self.cache.write_block(block_key, {'status': status, 'data': data})
        self.update_access(block_key)

    def is_cached(self, address):
        is_cached, block, block_key = False, None, 0
        for i in range(CACHE_BLOCKS):
            block = self.cache.blocks[i]
            if block['data'][0] == address:
                is_cached = True
                block_key = i
                break
        return is_cached, block, block_key

    def update_access(self, block_key):
        self.last_accessed_blocks.remove(block_key)
        self.last_accessed_blocks.insert(0, block_key)

    ########## Coherence ##########

    def read_cache(self, instruction):
        log(self.name, 'reading cache for ' + str(instruction))
        address = instruction['address']
        is_cached, block, block_key = self.is_cached(address)
        if not(is_cached):
            log(self.name, 'cache miss for ' + str(instruction))
            received_data = self.broadcast(instruction)
            if received_data: self.cache_new_data('S', received_data)
            elif not(received_data): 
                received_data = self.issue_mem_read(instruction)
                self.cache_new_data('E', received_data)
        elif block['status'] == "I":
            log(self.name, 'cache miss for ' + str(instruction))
            received_data = self.broadcast(instruction)
            if received_data: self.write_to_cache_block(block_key, 'S', received_data)
            elif not(received_data): 
                received_data = self.issue_mem_read(instruction)
                self.write_to_cache_block(block_key, 'E', received_data)
        else:
            received_data = block['data']
            self.update_access(block_key)
        return_value = received_data
        return return_value

    def write_cache(self, instruction):
        address, wr_value = instruction['address'], instruction['value']
        log(self.name, 'write cache for ' + str(bin(address)))
        is_cached, block, block_key = self.is_cached(address)
        if is_cached:
            status = block['status']
            if (status == "M" or status == "E"): self.cache.modify_block(block_key, wr_value)
            elif status == "S":
                self.broadcast(instruction)
                self.cache.modify_block(block_key, wr_value)
            elif status == "I":
                self.broadcast(instruction)
                self.cache.modify_block(block_key, wr_value)
            self.update_access(block_key)
        else:
            self.broadcast(instruction)
            self.cache_new_data('M', [address, wr_value])

    def process_CPU_instruction(self, instruction):
        log(self.name, 'processing ' + str(instruction))
        requested_value = 0
        match instruction['op_type']:
            case "READ": requested_value = self.read_cache(instruction)
            case "WRITE": self.write_cache(instruction)
        return requested_value

    def monitor_instruction(self, instruction):
        log(self.name, 'monitoring ' + str(instruction))
        response = None
        is_cached, block, block_key = self.is_cached(instruction['address'])
        if is_cached:
            response = self.apply_coherence_protocol(instruction, block, block_key)
        return response

    def apply_coherence_protocol(self, instruction, own_block, own_block_key):
        log(self.name, 'applying coherence for ' + str(instruction))
        is_read = (instruction['op_type'] == "READ")
        is_write = (instruction['op_type'] == "WRITE")
        response = None
        match own_block['status']:
            case 'M':
                self.writeback(own_block['data'])
                response = own_block['data']
                if is_read: self.cache.make_block_shared(own_block_key)
                elif is_write: self.cache.invalidate_block(own_block_key)
            case 'E':
                response = own_block['data']
                if is_read: self.cache.make_block_shared(own_block_key)
                elif is_write: self.cache.invalidate_block(own_block_key)
            case 'S':
                if is_read: response = own_block['data']
                elif is_write: self.cache.invalidate_block(own_block_key)
            case 'I':
                pass
        log(self.name, 'supplying data ' + str(response))
        return response

    def writeback(self, data):
        log(self.name, 'writeback ' + str(data))
        self.issue_mem_write({'CPU_ID': self.processor_ID, 'op_type': "WRITE", 'address': data[0], 'value': data[1]})
        
