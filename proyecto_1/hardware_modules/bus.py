from sys import path
path.append("../")
from constants import *

import memory, processor

class Bus:
    serialized_instructions = []
    connected_processors = []
    connected_memory = None

    def __init__(self):
        print("Bus created")

    def connect_processor(self, processor):
        self.connected_processors.append(processor)

    def connect_memory(self, memory):
        self.connected_memory = memory

    def transmit_instruction(self):
        print("Transmitting instruction!")

    def broadcast(self, processor_num, message):
        for i in self.connected_processors:
            if i != self.connected_processors[i].get_processor_ID():
                print("Broadcasting to all processors!")
