import time

from sys import path
path.append("../")
from constants import *

class Memory:
    blocks = {}
    #instruction_queue = []
    bus = None

    def __init__(self):
        self.create_blocks()
        self.log("created")

    def connect_bus(self, bus):
        self.bus = bus
        self.log("connected to bus")

    def create_blocks(self):
        for i in range(MEMORY_BLOCKS):
            self.blocks[MEMORY_BASE_ADDR+i] = 0x0

    """def get_instruction(self, instruction):
        self.instruction_queue += instruction"""

    """def execute_instructions(self):
        if (self.instruction_queue != []):
            time.sleep(MEM_ACCESS_PENALTY_TIME)
            self.log("executing instruction [0]")"""

    def execute_instruction(self, instruction):
        #time.sleep(MEM_ACCESS_PENALTY_TIME)
        data = None
        if instruction['op_type'] == "READ": data = self.read_mem(instruction['address'])
        elif instruction['op_type'] == "WRITE": self.write_mem(instruction['address'], instruction['value'])
        return data

    def read_mem(self, address):
        self.log("returning: " + str([address, self.blocks[address]]))
        return [address, self.blocks[address]]

    def write_mem(self, address, value):
        self.log(str(bin(address)) + " <- " + str(hex(value)))
        self.blocks[address] = value

    def log(self, message):
        print("[Memory]: " + message)
