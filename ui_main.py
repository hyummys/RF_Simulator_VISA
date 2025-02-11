#from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QCheckBox, QApplication, QTabWidget, QGroupBox
from PyQt5.QtWidgets import *
from app_func import *
from comm_set import *
from app_config import * 
from app_trxn import *
from app_info import *
from ui_displays import *

class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
        #MainWindow.resize(1000, 500)
        self.centralWidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralWidget)
        
        #creating Tab widgets
        self.tabWidgets = QTabWidget(self.centralWidget)

        #tabs
        # self.Comm_Set_tab(self.tabWidgets)
        self.Visa_Simulator_tab(self.tabWidgets)

        layout = QVBoxLayout(self.centralWidget)
        layout.addWidget(self.tabWidgets)

        #common values
        self.ser = None
        self.config_file = None
        self.config_file_path = None
        self.xml_file = None
        self.xml_file_path = None

        # self.trxn_window = None
        self.log_window = None

        self.trxn_list = None

    def Visa_Simulator_tab(self, tabWidgets):        
        pagelayout = QHBoxLayout()

        func_sector_ly = QVBoxLayout()

        ##################COMM SETTING#########################
        self.gb_comm = CommSet(main_window=self)
        self.gb_comm.btn_open_comm.clicked.connect(lambda: self.update_ser(self.gb_comm.ser) if self.gb_comm.btn_open_comm.text() == "Close" else self.update_ser(None))

        func_sector_ly.addWidget(self.gb_comm)


        ##################Configuration#########################
        self.Visa_config = VISA_FileConfig(main_window=self)
        func_sector_ly.addWidget(self.Visa_config)
        
        ##################Transaction#########################
        self.Visa_Trxn = VisaTrxnSet()
        func_sector_ly.addWidget(self.Visa_Trxn, 2)

        ##################Function Buttons#####################
        self.Visa_func = VISAFuncSet(main_window=self)
        func_sector_ly.addWidget(self.Visa_func, 2)

        ##################Host Server#########################
        self.gb_Host = VISADispInfo()
        func_sector_ly.addWidget(self.gb_Host, 1)

        ##################Window#########################
        self.visa_sim_ly = VisaDataWindows()
        
        pagelayout.addLayout(func_sector_ly, 1)
        pagelayout.addLayout(self.visa_sim_ly, 2)

        Visa_SIM = QWidget()
        Visa_SIM.setLayout(pagelayout)

        tabWidgets.addTab(Visa_SIM, "VISA")

    def Comm_Set_tab(self, tabWidgets):        
        pagelayout = QVBoxLayout()

        #Group box
        self.gb_comm = CommSet(main_window=self)

        pagelayout.addWidget(self.gb_comm)
        # pagelayout.addWidget(QLabel("Later..."))
        pagelayout.addStretch(1)

        #Comm Setting Widget
        Set_Comm = QWidget()
        Set_Comm.setLayout(pagelayout)

        #Tab
        tabWidgets.addTab(Set_Comm, "Setting")