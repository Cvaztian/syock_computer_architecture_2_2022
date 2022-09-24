from sys import path
path.append("../")
from common import *

class Cache:
    ########## Device creation ##########
    def __init__(self):
        self.ui_element = None
        self.blocks = {}
        self.create_blocks()

    def create_blocks(self):
        for i in range(CACHE_BLOCKS):
            self.blocks[i] = {'status': 'I', 'data': [0b0, 0x0]}

    ########## Cache blocks interaction ##########
    def modify_block(self, block_key, new_value):
        self.blocks[block_key]['status'] = 'M'
        self.blocks[block_key]['data'][1] = new_value
        self.update_ui_status(block_key)

    def make_block_exclusive(self, block_key):
        self.blocks[block_key]['status'] = 'E'
        self.update_ui_status(block_key)

    def make_block_shared(self, block_key):
        self.blocks[block_key]['status'] = 'S'
        self.update_ui_status(block_key)

    def invalidate_block(self, block_key):
        self.blocks[block_key]['status'] = 'I'
        self.update_ui_status(block_key)

    def write_block(self, block_key, block):
        self.blocks[block_key] = block
        self.update_ui_status(block_key)

    ########## Other ##########
    def print_cache(self):
        for i in range(CACHE_BLOCKS):
            print(self.blocks[i])

    ########## UI ##########

    def update_ui_status(self, block_key):
        index = str(block_key)
        status = self.blocks[block_key]['status']
        address = str(bin(self.blocks[block_key]['data'][0]))
        value = str(hex(self.blocks[block_key]['data'][1]))
        self.ui_element.modifyValueInCache(block_key, "{}: {}, {}, {}".format(index, status, address, value))
        print("UPDATING!!!!!!!!!!!!!!!!")
        print("{}: {}, {}, {}".format(index, status, address, value))
        print("UPDATING!!!!!!!!!!!!!!!!")

    def start_ui(self):
        for i in range(CACHE_BLOCKS):
            address = str(bin(0))
            value = str(hex(0))
            self.ui_element.addValueToCache("{}: {}, {}, {}".format(i, "I", address, value))
