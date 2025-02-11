import time
from PyQt5.QtWidgets import *
import serial
import serial.serialutil
import datetime
import format_resource as cmd
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QSizePolicy

class VISAFuncSet(QGroupBox):
    def __init__(self, parent=None, main_window=None):
        super(VISAFuncSet, self).__init__(parent)
        self.MainWindow = main_window

        self.setTitle('[Functions]')
        
        #Group Box
        Function_main_ly = QHBoxLayout()
        
        gb_Tool_functions = QGroupBox()

        self.btn_trxn_start = QPushButton("Transaction Start")
        self.btn_trxn_stop = QPushButton("Transaction Stop")
        self.btn_RF_off = QPushButton("RF Off")

        Tool_functions_ly = QHBoxLayout()

        # Tool_functions_ly.addWidget(self.btn_trxn_start, 0, 0)
        # Tool_functions_ly.addWidget(self.btn_trxn_stop, 0, 1)
        # Tool_functions_ly.addWidget(self.btn_RF_off, 0, 2)
        Tool_functions_ly.addWidget(self.btn_trxn_start)
        Tool_functions_ly.addWidget(self.btn_trxn_stop)
        Tool_functions_ly.addWidget(self.btn_RF_off)

        gb_Tool_functions.setLayout(Tool_functions_ly)

        Function_main_ly.addWidget(gb_Tool_functions)
        
        self.setLayout(Function_main_ly)
