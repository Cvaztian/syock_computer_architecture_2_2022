import random
import time

from sys import path
path.append("../")
from constants import *

from cache_controller import CacheController

class Processor:
    processor_ID = 0
    cache_controller = None
    bus = None

    def __init__(self, number, bus):
        self.processor_ID = number
        self.cache_controller = CacheController(number)
        self.bus = bus
        print("Created processor " + str(number))

    def get_processor_ID(self):
        return self.processor_ID

    def calc(self):
        time.sleep(1)

    def read_mem(self, address):
        print("Reading memory")

    def write_mem(self, address):
        print("Writing to memory")