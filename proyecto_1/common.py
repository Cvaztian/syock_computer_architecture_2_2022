import time
from constants import *

def print_banner(message):
    print("\n\n###### " + message + " ######\n")

def log(device, message):
    print("[{}]: {} ".format(device, message))

def wait_execution(seconds):
    time.sleep(seconds)

def connect_device_to_ui(device, ui_element):
    device.ui_element = ui_element