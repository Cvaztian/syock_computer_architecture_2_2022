import time
from constants import *

def print_banner(message):
    print("\n\n###### " + message + " ######\n")

def log(device, message):
    print("[{}]: {} ".format(device, message))

def wait_execution(seconds):
    time.sleep(seconds)
