from sys import path
path.append("./hardware_modules")

from constants import *
from processor import *
from memory import *
from bus import *

def start_simulation():
    print("###### Starting simulation ######\n")
    bus, memory, processors = create_devices()
    connect_devices(bus, memory, processors)

    start_processors(processors)
    
    print("\n###### Exiting simulation ######")
    return

def create_devices():
    print("###### Creating devices ######")
    bus = Bus()
    memory = Memory()
    processors = [Processor(i) for i in range(PROCESSOR_COUNT)]
    return bus, memory, processors

def connect_devices(bus, memory, processors):
    print("\n###### Connecting devices ######")
    bus.connect_memory(memory)
    memory.connect_bus(bus)
    for proc in processors:
        bus.connect_processor(proc)
        bus.connect_cache_controller(proc.cache_controller)
        proc.connect_bus(bus)
        proc.cache_controller.connect_bus(bus)
    print('\n')

def start_processors(processors):
    for proc in processors:
        proc.start_processor()

start_simulation()
