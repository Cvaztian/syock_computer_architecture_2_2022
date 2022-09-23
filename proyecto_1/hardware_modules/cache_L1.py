from sys import path
path.append("../")
from common import *

class Cache:
    ########## Device creation ##########
    def __init__(self):
        self.blocks = {}
        self.create_blocks()

    def create_blocks(self):
        for i in range(CACHE_BLOCKS):
            self.blocks[i] = {'status': 'I', 'data': [0b0, 0x0]}

    ########## Cache blocks interaction ##########
    def modify_block(self, block_key, new_value):
        self.blocks[block_key]['status'] = 'M'
        self.blocks[block_key]['data'][1] = new_value

    def make_block_exclusive(self, block_key):
        self.blocks[block_key]['status'] = 'E'

    def make_block_shared(self, block_key):
        self.blocks[block_key]['status'] = 'S'

    def invalidate_block(self, block_key):
        self.blocks[block_key]['status'] = 'I'

    def write_block(self, block_key, block):
        self.blocks[block_key] = block

    ########## Other ##########
    def print_cache(self):
        for i in range(CACHE_BLOCKS):
            print(self.blocks[i])
