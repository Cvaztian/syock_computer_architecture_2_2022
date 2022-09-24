


from PyQt5 import QtCore, QtGui, QtWidgets

class UI_Processor:
	def __init__(self,processorPanel) :
		self.processorPanel=processorPanel

	def setCPUValue(self, value): self.processorPanel.setText(value)

class UI_Control:
	def __init__(self,ControlPanel ) :
		self.controlPanel=ControlPanel

	def setControlValue(self, value):self.controlPanel.setText(value)

class UI_Cache:
	def __init__(self,cacheList:QtWidgets.QListWidget ) :
		self.cacheList =cacheList

	def addValueToCache(self,value):
		self.cacheList.addItem(value)

	def modifyValueInCache(self,index,value):
		self.cacheList.item(index)  .setText(value)


	def removeValueFromCache(self,index):
		self.cacheList.takeItem(index)


class UI_Bus:

	def __init__(self,bus ) :
		self.bus=bus

	def setBusValue(self, value):self.bus.setText(value)

class UI_Memory:
	def __init__(self,memory:QtWidgets.QListWidget ) :
		self.memory =memory

	def addValueToMem(self,value):
		self.memory.addItem(value)

	def modifyValueInMem(self,index,value):
		self.memory.item(index)  .setText(value)


	def removeValueFromMem(self,index):
		self.memory.takeItem(index)


class Ui_MainWindow(object):

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1140, 910)
		MainWindow.setStyleSheet("")
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setEnabled(True)
		self.groupBox.setGeometry(QtCore.QRect(40, 20, 251, 321))
		self.groupBox.setStyleSheet("border-style: outset;\n"
		"    border-width: 2px;\n"
		"    border-color: gray;")
		self.groupBox.setTitle("")
		self.groupBox.setProperty("lineWidth", 32)
		self.groupBox.setObjectName("groupBox")
		self.CPU1Title = QtWidgets.QLabel(self.groupBox)
		self.CPU1Title.setGeometry(QtCore.QRect(140, 30, 91, 31))
		self.CPU1Title.setObjectName("CPU1Title")
		self.CPU1Data = QtWidgets.QLabel(self.groupBox)
		self.CPU1Data.setGeometry(QtCore.QRect(140, 60, 91, 51))
		self.CPU1Data.setObjectName("CPU1Data")
		self.Control1Title = QtWidgets.QLabel(self.groupBox)
		self.Control1Title.setGeometry(QtCore.QRect(20, 30, 91, 31))
		self.Control1Title.setObjectName("Control1Title")
		self.ControlData1 = QtWidgets.QLabel(self.groupBox)
		self.ControlData1.setGeometry(QtCore.QRect(20, 60, 91, 51))
		self.ControlData1.setObjectName("ControlData1")
		self.CacheList1 = QtWidgets.QListWidget(self.groupBox)
		self.CacheList1.setGeometry(QtCore.QRect(20, 170, 211, 131))
		self.CacheList1.setObjectName("CacheList1")
		self.CacheL1 = QtWidgets.QLabel(self.groupBox)
		self.CacheL1.setGeometry(QtCore.QRect(20, 140, 211, 31))
		self.CacheL1.setObjectName("CacheL1")
		self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_2.setEnabled(True)
		self.groupBox_2.setGeometry(QtCore.QRect(310, 20, 251, 321))
		self.groupBox_2.setStyleSheet("border-style: outset;\n"
		"    border-width: 2px;\n"
		"    border-color: gray;")
		self.groupBox_2.setTitle("")
		self.groupBox_2.setProperty("lineWidth", 32)
		self.groupBox_2.setObjectName("groupBox_2")
		self.CPU1Title_2 = QtWidgets.QLabel(self.groupBox_2)
		self.CPU1Title_2.setGeometry(QtCore.QRect(140, 30, 91, 31))
		self.CPU1Title_2.setObjectName("CPU1Title_2")
		self.CPU2Data = QtWidgets.QLabel(self.groupBox_2)
		self.CPU2Data.setGeometry(QtCore.QRect(140, 60, 91, 51))
		self.CPU2Data.setObjectName("CPU2Data")
		self.Control1Title_2 = QtWidgets.QLabel(self.groupBox_2)
		self.Control1Title_2.setGeometry(QtCore.QRect(20, 30, 91, 31))
		self.Control1Title_2.setObjectName("Control1Title_2")
		self.ControlData2 = QtWidgets.QLabel(self.groupBox_2)
		self.ControlData2.setGeometry(QtCore.QRect(20, 60, 91, 51))
		self.ControlData2.setObjectName("ControlData2")
		self.CacheList2 = QtWidgets.QListWidget(self.groupBox_2)
		self.CacheList2.setGeometry(QtCore.QRect(20, 170, 211, 131))
		self.CacheList2.setObjectName("CacheList2")
		self.CacheL2 = QtWidgets.QLabel(self.groupBox_2)
		self.CacheL2.setGeometry(QtCore.QRect(20, 140, 211, 31))
		self.CacheL2.setObjectName("CacheL2")
		self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_3.setEnabled(True)
		self.groupBox_3.setGeometry(QtCore.QRect(580, 20, 251, 321))
		self.groupBox_3.setStyleSheet("border-style: outset;\n"
		"    border-width: 2px;\n"
		"    border-color: gray;")
		self.groupBox_3.setTitle("")
		self.groupBox_3.setProperty("lineWidth", 32)
		self.groupBox_3.setObjectName("groupBox_3")
		self.CPU1Title_4 = QtWidgets.QLabel(self.groupBox_3)
		self.CPU1Title_4.setGeometry(QtCore.QRect(140, 30, 91, 31))
		self.CPU1Title_4.setObjectName("CPU1Title_4")
		self.CPU3Data = QtWidgets.QLabel(self.groupBox_3)
		self.CPU3Data.setGeometry(QtCore.QRect(140, 60, 91, 51))
		self.CPU3Data.setObjectName("CPU3Data")
		self.Control1Title_4 = QtWidgets.QLabel(self.groupBox_3)
		self.Control1Title_4.setGeometry(QtCore.QRect(20, 30, 91, 31))
		self.Control1Title_4.setObjectName("Control1Title_4")
		self.ControlData3 = QtWidgets.QLabel(self.groupBox_3)
		self.ControlData3.setGeometry(QtCore.QRect(20, 60, 91, 51))
		self.ControlData3.setObjectName("ControlData3")
		self.CacheList3 = QtWidgets.QListWidget(self.groupBox_3)
		self.CacheList3.setGeometry(QtCore.QRect(20, 170, 211, 131))
		self.CacheList3.setObjectName("CacheList3")
		self.CacheL3 = QtWidgets.QLabel(self.groupBox_3)
		self.CacheL3.setGeometry(QtCore.QRect(20, 140, 211, 31))
		self.CacheL3.setObjectName("CacheL3")
		self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_4.setEnabled(True)
		self.groupBox_4.setGeometry(QtCore.QRect(850, 20, 251, 321))
		self.groupBox_4.setStyleSheet("border-style: outset;\n"
		"    border-width: 2px;\n"
		"    border-color: gray;")
		self.groupBox_4.setTitle("")
		self.groupBox_4.setProperty("lineWidth", 32)
		self.groupBox_4.setObjectName("groupBox_4")
		self.CPU1Title_5 = QtWidgets.QLabel(self.groupBox_4)
		self.CPU1Title_5.setGeometry(QtCore.QRect(140, 30, 91, 31))
		self.CPU1Title_5.setObjectName("CPU1Title_5")
		self.CPU4Data = QtWidgets.QLabel(self.groupBox_4)
		self.CPU4Data.setGeometry(QtCore.QRect(140, 60, 91, 51))
		self.CPU4Data.setObjectName("CPU4Data")
		self.Control1Title_5 = QtWidgets.QLabel(self.groupBox_4)
		self.Control1Title_5.setGeometry(QtCore.QRect(20, 30, 91, 31))
		self.Control1Title_5.setObjectName("Control1Title_5")
		self.ControlData4 = QtWidgets.QLabel(self.groupBox_4)
		self.ControlData4.setGeometry(QtCore.QRect(20, 60, 91, 51))
		self.ControlData4.setObjectName("ControlData4")
		self.CacheList4 = QtWidgets.QListWidget(self.groupBox_4)
		self.CacheList4.setGeometry(QtCore.QRect(20, 170, 211, 131))
		self.CacheList4.setObjectName("CacheList5")
		self.CacheL4 = QtWidgets.QLabel(self.groupBox_4)
		self.CacheL4.setGeometry(QtCore.QRect(20, 140, 211, 31))
		self.CacheL4.setObjectName("CacheL4")
		self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_5.setGeometry(QtCore.QRect(40, 389, 1061, 81))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(False)
		font.setWeight(50)
		self.groupBox_5.setFont(font)
		self.groupBox_5.setStyleSheet("border-style: outset;\n"
		"    border-width: 2px;\n"
		"    border-color: gray;")
		self.groupBox_5.setTitle("Bus")
		self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
		self.groupBox_5.setObjectName("groupBox_5")
		self.BusData = QtWidgets.QLabel(self.groupBox_5)
		self.BusData.setGeometry(QtCore.QRect(0, 20, 1061, 61))
		font = QtGui.QFont()
		font.setPointSize(12)
		font.setBold(True)
		font.setWeight(75)
		font.setKerning(False)
		self.BusData.setFont(font)
		self.BusData.setLayoutDirection(QtCore.Qt.RightToLeft)
		self.BusData.setAlignment(QtCore.Qt.AlignCenter)
		self.BusData.setObjectName("BusData")
		self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_6.setEnabled(True)
		self.groupBox_6.setGeometry(QtCore.QRect(400, 510, 341, 231))
		font = QtGui.QFont()
		font.setPointSize(11)
		self.groupBox_6.setFont(font)
		self.groupBox_6.setStyleSheet("border-style: outset;\n"
		"    border-width: 2px;\n"
		"    border-color: gray;")
		self.groupBox_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
		self.groupBox_6.setProperty("lineWidth", 32)
		self.groupBox_6.setObjectName("groupBox_6")
		self.MemoryList = QtWidgets.QListWidget(self.groupBox_6)
		self.MemoryList.setGeometry(QtCore.QRect(20, 25, 291, 190))
		self.MemoryList.setObjectName("MemoriaList")
		self.line = QtWidgets.QFrame(self.centralwidget)
		self.line.setGeometry(QtCore.QRect(153, 340, 20, 51))
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.line_2 = QtWidgets.QFrame(self.centralwidget)
		self.line_2.setGeometry(QtCore.QRect(430, 340, 20, 51))
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.line_3 = QtWidgets.QFrame(self.centralwidget)
		self.line_3.setGeometry(QtCore.QRect(700, 340, 20, 51))
		self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_3.setObjectName("line_3")
		self.line_4 = QtWidgets.QFrame(self.centralwidget)
		self.line_4.setGeometry(QtCore.QRect(970, 340, 20, 51))
		self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_4.setObjectName("line_4")
		self.line_5 = QtWidgets.QFrame(self.centralwidget)
		self.line_5.setGeometry(QtCore.QRect(560, 470, 20, 41))
		self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_5.setObjectName("line_5")

		self.startButton = QtWidgets.QPushButton(self.centralwidget)
		self.startButton.setGeometry(QtCore.QRect(550, 800, 51, 21))
		self.startButton.setText("Start")
		self.stopButton = QtWidgets.QPushButton(self.centralwidget)
		self.stopButton.setGeometry(QtCore.QRect(500, 800, 51, 21))
		self.stopButton.setText("Stop")
		self.stepButton = QtWidgets.QPushButton(self.centralwidget)
		self.stepButton.setGeometry(QtCore.QRect(600, 800, 51, 21))
		self.stepButton.setText("Step")


		self.inputBar = QtWidgets.QLineEdit(self.centralwidget)
		self.inputBar.setGeometry(QtCore.QRect(130, 800, 200, 21))
		


		self.inputButton = QtWidgets.QPushButton(self.centralwidget)
		self.inputButton.setGeometry(QtCore.QRect(350, 800, 51, 21))
		self.inputButton.setText("Send")


		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 25))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.createComponents()
		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):

		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.CPU1Title.setText(_translate("MainWindow", "CPU1"))
		self.CPU1Data.setText(_translate("MainWindow", ""))
		self.Control1Title.setText(_translate("MainWindow", "Control"))
		self.ControlData1.setText(_translate("MainWindow", ""))
		self.CacheL1.setText(_translate("MainWindow", "Caché L1"))
		self.CPU1Title_2.setText(_translate("MainWindow", "CPU2"))
		self.CPU2Data.setText(_translate("MainWindow", ""))
		self.Control1Title_2.setText(_translate("MainWindow", "Control"))
		self.ControlData3.setText(_translate("MainWindow", ""))
		self.CacheL2.setText(_translate("MainWindow", "Caché L2"))
		self.CPU1Title_4.setText(_translate("MainWindow", "CPU3"))
		self.CPU2Data.setText(_translate("MainWindow", ""))
		self.Control1Title_4.setText(_translate("MainWindow", "Control"))
		self.ControlData3.setText(_translate("MainWindow", ""))
		self.CacheL3.setText(_translate("MainWindow", "Caché L3"))
		self.CPU1Title_5.setText(_translate("MainWindow", "CPU4"))
		self.CPU4Data.setText(_translate("MainWindow", ""))
		self.Control1Title_5.setText(_translate("MainWindow", "Control"))
		self.ControlData4.setText(_translate("MainWindow", ""))
		self.CacheL4.setText(_translate("MainWindow", "Caché L4"))
		self.BusData.setText(_translate("MainWindow", "Bus"))
		self.groupBox_6.setTitle(_translate("MainWindow", "Memoria"))





	def addValueToMemory(self,value):
		self.MemoryList.addItem(value)


	def modifyValueInMemory(self,index,value):
		self.MemoryList.item(index)  .setText(value)

	def removeValueFromMemory(self,index):
		self.MemoryList.takeItem(index)

	def setBusAction(self, value): self.BusData.setText(value)

	def createComponents(self):
		self.processors= []
		self.controllers= []
		self.caches= []

		self.processors.append(UI_Processor(self.CPU1Data,))
		self.processors.append(UI_Processor(self.CPU2Data))
		self.processors.append(UI_Processor(self.CPU3Data))
		self.processors.append(UI_Processor(self.CPU4Data))


		self.controllers.append(UI_Control(self.ControlData1))
		self.controllers.append(UI_Control(self.ControlData2))
		self.controllers.append(UI_Control(self.ControlData3))
		self.controllers.append(UI_Control(self.ControlData4))

		self.caches.append(UI_Cache(self.CacheList1))
		self.caches.append(UI_Cache(self.CacheList2))
		self.caches.append(UI_Cache(self.CacheList3))
		self.caches.append(UI_Cache(self.CacheList4))

		self.memory =UI_Memory(self.MemoryList)

		self.bus = UI_Bus(self.BusData)


	def getProcessor(self, cpuId)-> UI_Processor:
		return self.processors[cpuId]

	def getController(self, id)-> UI_Control:
		return self.controllers[id]

	def getCache(self, id)-> UI_Cache:
		return self.caches[id]



	def getProcessors(self):
		
		return self.processors

	def getValueFromInput(self):
		return self.inputBar.text()

