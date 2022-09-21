from dis import Instruction
from sys import path
path.append("../")
from constants import *

from cache_L1 import Cache

class CacheController:
    bus = None
    cache = Cache()
    processor_ID = 0
    last_accessed_blocks = [i for i in range(CACHE_BLOCKS)]

    ########## Device creation ##########

    def __init__(self, number):
        self.processor_ID = number
        self.log("created")

    def connect_bus(self, bus):
        self.bus = bus
        self.log("connected to bus")

    ########## Communication ##########

    def issue_mem_read(self, instruction):
        return [MEMORY_BASE_ADDR, 7]

    def issue_mem_write(self, instruction):
        self.bus.transmit_instruction(instruction)

    def broadcast(self, instruction):
        self.log("broadcasting " + str(instruction))
        data = self.bus.propagate_broadcast(instruction)
        return data

    def get_processor_ID(self):
        return self.processor_ID

    ########## Cache control ##########

    def cache_new_data(self, status, data):
        least_used_key = self.last_accessed_blocks[-1]
        self.log('caching new block ' + str(least_used_key) + str({'status': status, 'data': data}))
        self.cache.write_block(least_used_key, {'status': status, 'data': data})
        self.update_access(least_used_key)

    def write_to_cache_block(self, block_key, status, data):
        self.log('writing to cache block ' + str(block_key) + str({'status': status, 'data': data}))
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
        self.log('reading cache for ' + str(instruction))
        address = instruction['address']
        is_cached, block, block_key = self.is_cached(address)
        if not(is_cached):
            self.log('cache miss for ' + str(instruction))
            received_data = self.broadcast(instruction)
            if received_data: self.cache_new_data('S', received_data)
            elif not(received_data): 
                received_data = self.issue_mem_read(instruction)
                self.cache_new_data('E', received_data)
        elif block['status'] == "I":
            self.log('cache miss for ' + str(instruction))
            received_data = self.broadcast(instruction)
            if received_data: self.write_to_cache_block(block_key, 'S', received_data)
            elif not(received_data): 
                received_data = self.issue_mem_read(instruction)
                self.write_to_cache_block(block_key, 'E', received_data)
        else: received_data = block['data']
        return_value = received_data
        return return_value

    def write_cache(self, instruction):
        address, wr_value = instruction['address'], instruction['value']
        is_cached, block, block_key = self.is_cached(address)
        if is_cached:
            if (block['status'] == "M" or block['status'] == "E"): self.cache.modify_block(block_key, wr_value)
            elif block['status'] == "S":
                self.broadcast(instruction)
                self.cache.modify_block(block_key, wr_value)
            elif block['status'] == "I":
                received_data = self.broadcast(instruction)
                if not(received_data): received_data = self.issue_mem_read(instruction)
                self.cache.modify_block(block_key, wr_value)
        else:
            #received_data = self.broadcast(instruction)
            #if not(received_data): received_data = self.issue_mem_read(instruction)
            self.cache_new_data('M', [address, wr_value])

    def process_CPU_instruction(self, instruction):
        self.log('processing ' + str(instruction))
        requested_value = 0
        match instruction['op_type']:
            case "read": requested_value = self.read_cache(instruction)
            case "write": self.write_cache(instruction)
        return requested_value

    def monitor_instruction(self, instruction):
        self.log('monitoring ' + str(instruction))
        response = None
        is_cached, block, block_key = self.is_cached(instruction['address'])
        if is_cached:
            response = self.apply_coherence_protocol(instruction, block, block_key)
            self.log("received " + str(instruction))
        return response

    def apply_coherence_protocol(self, instruction, own_block, own_block_key):
        self.log('applying coherence for ' + str(instruction))
        is_read = (instruction['op_type'] == "read")
        is_write = (instruction['op_type'] == "write")
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
        self.log('supplying data ' + str(response))
        return response

    def writeback(self, data):
        self.log('writeback ' + data)
        self.issue_mem_write([self.processor_ID, "write", data[0], data[1]])

    def log(self, message):
        print("[Cache controller " + str(self.processor_ID) + "]: " + message)




    """def share_exclusive_block(self, block_key):
        self.cache.blocks[block_key][0] = "S"
        return self.cache.blocks[block_key]
        
    def get_from_another_cache(self, address):
        exclusive_block = []
        for controller in self.bus.connected_controllers:
            is_cached, block, block_key = controller.is_cached(address)
            if is_cached and block[0] == "E":
                exclusive_block = controller.share_exclusive_block(block_key)
                break
        return exclusive_block
    """