from sys import path
path.append("../")
from common import *

class Bus:
    ui_element = None
    name = "Bus"
    connected_cache_controllers = []
    connected_processors = []
    connected_memory = None

    ########## Device creation ##########
    def __init__(self):
        log(self.name, "created")

    def connect_processor(self, processor):
        self.connected_processors.append(processor)

    def connect_cache_controller(self, controller):
        self.connected_cache_controllers.append(controller)

    def connect_memory(self, memory):
        self.connected_memory = memory

    ########## Communication ##########
    def transmit_instruction(self, instruction):
        self.update_ui_status("Transmitting {}".format(str(instruction)))
        data = self.connected_memory.execute_instruction(instruction)
        self.update_ui_status("")
        return data

    def propagate_broadcast(self, instruction):
        self.update_ui_status("Broadcasting {}".format(str(instruction)))
        broadcaster_ID = instruction['CPU_ID']
        return_data = None
        for controller in self.connected_cache_controllers:
            if controller.processor_ID != broadcaster_ID:
                response = controller.monitor_instruction(instruction)
                if response: return_data = response
        log(self.name, "supplying " + str(response))
        self.update_ui_status("Supplying {}".format(str(response)))
        self.update_ui_status("")
        return return_data

    ########## Other ##########
    def get_cache_controller(self, controller_ID):
        for controller in self.connected_cache_controllers:
            if controller.processor_ID == controller_ID: return controller

    def update_ui_status(self, message):
        self.ui_element.setBusValue(message)
        wait_execution(ACCESS_TIME)

