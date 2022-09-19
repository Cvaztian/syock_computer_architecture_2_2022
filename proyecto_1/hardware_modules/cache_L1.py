from sys import path
path.append("../")
from constants import *

class Cache:
    blocks = {}

    def __init__(self):
        self.create_blocks()

    def create_blocks(self):
        for i in range(CACHE_BLOCKS):
            self.blocks[i] = ['I', 0b0, 0x0]

    def modify_block(self, block_num, new_value):
        self.blocks[block_num][0] = 'M'
        self.blocks[block_num][2] = new_value

    def make_block_exclusive(self, block_num):
        self.blocks[block_num][0] = 'E'

    def make_block_shared(self, block_num):
        self.blocks[block_num][0] = 'S'

    def invalidate_block(self, block_num):
        self.blocks[block_num][0] = 'I'

    def read_block(self, address):
        value = "MISS"
        for i in range(CACHE_BLOCKS):
            if(self.blocks[i][1] == address):
                value = self.blocks[i][2]
                break
        return value