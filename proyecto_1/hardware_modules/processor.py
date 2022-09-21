import time
from random import choice, randint
from sys import path
path.append("../")
from constants import *

from cache_controller import CacheController

class Processor:
    processor_ID = 0
    cache_controller = None
    bus = None

    def __init__(self, number):
        self.processor_ID = number
        self.log("created")
        self.cache_controller = CacheController(number)

    def get_processor_ID(self):
        return self.processor_ID

    def connect_bus(self, bus):
        self.bus = bus
        self.log("connected to bus")

    def calc(self):
        self.log("calc")
        time.sleep(ACCESS_TIME)

    def generate_instruction(self):
        op_type = choice((0, 1))
        address = MEMORY_BASE_ADDR + randint(0, 7)
        if op_type == 0: return {'CPU_ID': self.processor_ID, 'op_type': 'read', 'address': address}
        else: return {'CPU_ID': self.processor_ID, 'op_type': 'write', 'address': address, 'value': 5}

    def start_processor(self):
        for i in range(10):
            instruction = self.generate_instruction()
            self.cache_controller.process_CPU_instruction(instruction)

    def single_run(self):
        instruction = self.generate_instruction()
        print(self.cache_controller.process_CPU_instruction(instruction))

    def log(self, message):
        print("[Processor " + str(self.processor_ID) + "]: " + message)
