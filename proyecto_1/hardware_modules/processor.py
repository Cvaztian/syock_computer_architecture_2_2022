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
        # Processor information
        self.ui_element = None
        self.name = "Processor" + str(number)
        self.processor_ID = number
        # Connected devices
        self.cache_controller = CacheController(number)
        self.bus = None
        # Processor control
        self.next_instruction = None
        self.waiting = False
        self.stop = False
        log(self.name, "created")

    def connect_bus(self, bus):
        self.bus = bus
        log(self.name, "connected to bus")

    def set_next_instruction(self, instruction):
        log(self.name, "received instruction")
        is_write = (len(instruction) == 4)
        if is_write: self.next_instruction = {'CPU_ID': self.processor_ID, 'op_type': "WRITE", 'address': int(instruction[2]), 'value': int(instruction[3])}
        else: self.next_instruction = {'CPU_ID': self.processor_ID, 'op_type': "READ", 'address': int(instruction[2])}
    
    ########## Instruction generation ##########
    def calc(self):
        log(self.name, "CALC")
        self.update_ui_status("CALC")
        wait_execution(ACCESS_TIME)

    def generate_instruction(self, op_type):
        if self.next_instruction != None:
            instruction = self.next_instruction
            self.next_instruction = None
        else:
            address = MEMORY_BASE_ADDR + self.random_address()
            if op_type == READ:
                instruction = {'CPU_ID': self.processor_ID, 'op_type': "READ", 'address': address}
                self.update_ui_status("P{}: READ {}".format(self.processor_ID, bin(address)))
            elif op_type == WRITE:
                value = randint(0, 255)
                instruction = {'CPU_ID': self.processor_ID, 'op_type': "WRITE", 'address': address, 'value': value}
                self.update_ui_status("P{}: WRITE {} {}".format(self.processor_ID, bin(address), hex(value)))
        return instruction

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
        log(self.name, "waiting")

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

    def update_ui_status(self, message):
        self.ui_element.setCPUValue(message)
        wait_execution(ACCESS_TIME)
