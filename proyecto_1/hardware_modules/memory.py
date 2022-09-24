from audioop import add
from sys import path
path.append("../")
from common import *

class Memory:
    ui_element = None
    name = "Memory"
    blocks = {}
    bus = None

    ########## Communication ##########
    def __init__(self):
        self.create_blocks()
        log(self.name, "created")

    def connect_bus(self, bus):
        self.bus = bus
        log(self.name, "connected to bus")

    def create_blocks(self):
        for i in range(MEMORY_BLOCKS):
            self.blocks[MEMORY_BASE_ADDR+i] = 0x0

    def execute_instruction(self, instruction):
        data = None
        if instruction['op_type'] == "READ": 
            wait_execution(MEM_ACCESS_PENALTY_TIME)
            data = self.read_mem(instruction['address'])
        elif instruction['op_type'] == "WRITE": self.write_mem(instruction['address'], instruction['value'])
        return data

    def read_mem(self, address):
        log(self.name, "returning: " + str([address, self.blocks[address]]))
        return [address, self.blocks[address]]

    def write_mem(self, address, value):
        log(self.name, str(bin(address)) + " <- " + str(hex(value)))
        self.blocks[address] = value
        self.update_ui_status(address, value)

    ########## Coherence ##########

    def update_ui_status(self, address, value):
        if self.ui_element:
            index = list(self.blocks.keys()).index(address)
            address = str(bin(address))
            value = str(hex(value))
            self.ui_element.modifyValueInMem(index, "{}: {}".format(address, value))

    def start_ui(self):
        if self.ui_element:
            for i in range(MEMORY_BLOCKS):
                address = str(bin(MEMORY_BASE_ADDR+i))
                value = str(hex(0))
                self.ui_element.addValueToMem("{}: {}".format(address, value))
