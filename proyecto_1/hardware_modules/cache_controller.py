from sys import path
path.append("../")
from constants import *

from cache_L1 import Cache
from bus import Bus

class CacheController:
    bus = None
    cache = Cache()
    processor_num = 0

    def __init__(self, number):
        self.processor_num = number

    def connect_bus(self, bus):
        self.bus = bus

    def broadcast(self, message):
        self.bus.broadcast(self.processor_num, message)

    def send_message(self):
        print("Sending message")
