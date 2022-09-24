from threading import Thread

from ui import *
from simulation import *

def connect_devices_to_ui(simulation):
    global ui
    connect_device_to_ui(simulation.bus, ui.bus)
    connect_device_to_ui(simulation.memory, ui.memory)
    for i in range(len(ui.processors)): 
        connect_device_to_ui(simulation.processors[i], ui.processors[i])
        connect_device_to_ui(simulation.processors[i].cache_controller, ui.controllers[i])
        connect_device_to_ui(simulation.processors[i].cache_controller.cache, ui.caches[i])

def initiate_ui_elements(simulation):
    for proc in simulation.processors:
        proc.cache_controller.cache.start_ui()
    simulation.memory.start_ui()

def start_ui():
    global ui
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    simulation = Simulation()
    connect_devices_to_ui(simulation)
    initiate_ui_elements(simulation)
    sim_thread = Thread(target=simulation.start_simulation)
    
    ui.startButton.clicked.connect(lambda: sim_thread.start())
    ui.stopButton.clicked.connect(lambda: simulation.pause_resume_simulation())
    ui.stepButton.clicked.connect(lambda: simulation.run_single_cycle())
    ui.inputButton.clicked.connect(lambda: simulation.input_instruction(ui.getValueFromInput()))

    MainWindow.show()
    app.exec_()

start_ui()
