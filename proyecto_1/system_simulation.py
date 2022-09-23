from threading import Thread, Lock
from sys import path
path.append("./hardware_modules")

from constants import *
from common import *
from processor import *
from memory import *
from bus import *

def start_simulation():
    print_banner("Starting simulation")
    bus, memory, processors = create_devices()
    connect_devices(bus, memory, processors)

    run_processors(processors)
    print_all_caches(processors)

    print_banner("Exiting simulation")
    return

def create_devices():
    print_banner("Creating devices")
    bus = Bus()
    memory = Memory()
    processors = [Processor(i) for i in range(PROCESSOR_COUNT)]
    return bus, memory, processors

def connect_devices(bus, memory, processors):
    print_banner("Connecting devices")
    bus.connect_memory(memory)
    memory.connect_bus(bus)
    for proc in processors:
        bus.connect_processor(proc)
        bus.connect_cache_controller(proc.cache_controller)
        proc.connect_bus(bus)
        proc.cache_controller.connect_bus(bus)

def run_processors(processors):
    thread_lock = Lock()
    threads = []
    for proc in processors:
        thread = Thread(target=proc.run_processor, args=(thread_lock,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def print_all_caches(processors):
    for proc in processors:
        print_banner("Cache state for " + str(proc.processor_ID))
        proc.cache_controller.cache.print_cache()

start_simulation()
