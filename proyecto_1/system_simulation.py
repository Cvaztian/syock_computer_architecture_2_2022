from sys import path
path.append("./hardware_modules")

from constants import *
from processor import *
from memory import *
from bus import *

def start_simulation():
    print("Starting simulation")
    bus, memory, processors = create_devices()
    connect_devices(bus, memory, processors)
    print("Exiting simulation")
    return

def create_devices():
    print("Creating devices")
    bus = Bus()
    memory = Memory(bus)
    processors = [Processor(i, bus) for i in range(PROCESSOR_COUNT)]
    return bus, memory, processors

def connect_devices(bus, memory, processors):
    print("Connecting devices")
    for i in range(PROCESSOR_COUNT):
        bus.connect_processor(processors[i])
    bus.connect_memory(memory)

start_simulation()
