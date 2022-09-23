from random import uniform, randint
from math import e

from sys import path
path.append("../")
from common import *

from cache_controller import CacheController

CALC = 0
READ = 1
WRITE = 2

class Processor:
    ########## Device creation ##########
    def __init__(self, number):
        self.name = "Processor" + str(number)
        self.processor_ID = number
        self.cache_controller = CacheController(number)
        self.bus = None
        self.waiting = False
        self.stop = False
        log(self.name, "created")

    def connect_bus(self, bus):
        self.bus = bus
        log(self.name, "connected to bus")

    
    ########## Instruction generation ##########
    def calc(self):
        log(self.name, "CALC")
        wait_execution(ACCESS_TIME)

    def generate_instruction(self, op_type):
        address = MEMORY_BASE_ADDR + self.random_address()
        if op_type == READ: return {'CPU_ID': self.processor_ID, 'op_type': "READ", 'address': address}
        elif op_type == WRITE: return {'CPU_ID': self.processor_ID, 'op_type': "WRITE", 'address': address, 'value': randint(0, 500)}

    def random_op(self):
        lambd = 5
        random_num = self.get_poisson(lambd)
        return random_num % 3

    def random_address(self):
        random_num = self.get_poisson(MEMORY_BLOCKS)
        return random_num % MEMORY_BLOCKS

    def get_poisson(self, lambd):
        e_inv = e**(-lambd)
        fraction = 1.0
        counter = 0
        while(fraction > e_inv):
            counter+=1
            fraction *= uniform(0,1)
        return counter-1

    ########## Device flow and control ##########
    def run_processor(self, thread_lock):
        while(not(self.stop)):
            if(not(self.waiting)):
                self.run_cycle(thread_lock)

    def stop_processor(self):
        self.stop = True
        log(self.name, "stopped")

    def wait(self):
        self.waiting = True

    def run_cycle(self, thread_lock):
        op_type = self.random_op()
        if op_type == CALC: self.calc()
        else:
            instruction = self.generate_instruction(op_type)
            thread_lock.acquire()
            log(self.name, "Lock acquired")
            self.cache_controller.process_CPU_instruction(instruction)
            wait_execution(ACCESS_TIME)
            print('Completed instruction!\n')
            thread_lock.release()
