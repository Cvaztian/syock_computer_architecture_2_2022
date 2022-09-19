import time

from sys import path
path.append("../")
from constants import *

class Memory:
    blocks = {}
    instruction_queue = []
    bus = None

    def __init__(self, bus):
        self.create_blocks()
        self.bus = bus
        print("Memory created")

    def create_blocks(self):
        for i in range(MEMORY_BLOCKS):
            self.blocks[MEMORY_BASE_ADDR+i] = [0x0]

    def get_instruction(self, instruction):
        self.instruction_queue += instruction

    def execute_instructions(self):
        if (self.instruction_queue != []):
            time.sleep(3)
            print("Executing instruction [0]")
    
    def read_mem(self, address):
        print("Reading from memory")

    def write_mem(self, address, value):
        print("Writing to memory")

