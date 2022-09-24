from threading import Thread, Lock
import sys
sys.path.append("./hardware_modules")

from ui import *
from constants import *
from common import *
from processor import *
from memory import *
from bus import *

class Simulation:
    def __init__(self):
        self.processors, self.memory, self.bus = self.create_devices()
        self.connect_devices_to_bus()

    def create_devices(self):
        print_banner("Creating devices")
        processors = [Processor(i) for i in range(PROCESSOR_COUNT)]
        memory = Memory()
        bus = Bus()
        return processors, memory, bus

    def connect_devices_to_bus(self):
        print_banner("Connecting devices")
        self.bus.connect_memory(self.memory)
        self.memory.connect_bus(self.bus)
        for proc in self.processors:
            self.bus.connect_processor(proc)
            self.bus.connect_cache_controller(proc.cache_controller)
            proc.connect_bus(self.bus)
            proc.cache_controller.connect_bus(self.bus)

    def run_processors(self):
        thread_lock = Lock()
        threads = []
        for proc in self.processors:
            thread = Thread(target=proc.run_processor, args=(thread_lock,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()

    def input_instruction(self, input):
        instruction = input.replace(" ", "")
        instruction = instruction.split(",")
        index = int(instruction[0])
        self.processors[index].set_next_instruction(instruction)

    def print_all_caches(self):
        for proc in self.processors:
            print_banner("Cache state for " + str(proc.processor_ID))
            proc.cache_controller.cache.print_cache()

    def start_simulation(self):
        print_banner("Starting simulation")
        
        self.run_processors()
        self.print_all_caches()

        print_banner("Exiting simulation")
        return

    def pause_resume_simulation(self):
        for proc in self.processors: proc.waiting = not(proc.waiting)

    def run_single_cycle(self):
        for proc in self.processors: proc.run_cycle()