from sys import path
path.append("../")
from constants import *

import memory, processor

class Bus:
    serialized_instructions = []

    connected_cache_controllers = []
    connected_processors = []
    connected_memory = None

    def __init__(self):
        print("Bus created")

    def connect_processor(self, processor):
        self.connected_processors.append(processor)

    def connect_cache_controller(self, controller):
        self.connected_cache_controllers.append(controller)

    def connect_memory(self, memory):
        self.connected_memory = memory

    def transmit_instruction(self, instruction):
        print("Transmitting instruction!")

    def get_cache_controller(self, controller_ID):
        for controller in self.connected_cache_controllers:
            if controller.get_processor_ID() == controller_ID: return controller

    def propagate_broadcast(self, instruction):
        broadcaster_ID = instruction['CPU_ID']
        return_data = None
        for controller in self.connected_cache_controllers:
            if controller.get_processor_ID() != broadcaster_ID:
                response = controller.monitor_instruction(instruction)
                if response: return_data = response
        return return_data
