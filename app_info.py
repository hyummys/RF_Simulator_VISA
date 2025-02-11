from PyQt5.QtWidgets import *
import sys

class VISADispInfo(QGroupBox):
    def __init__(self, parent=None, main_window=None):
        super(VISADispInfo, self).__init__(parent)
        self.MainWindow = main_window
        self.setTitle('[Ver & Checksum]')

        main_ly = QVBoxLayout()
        self.setLayout(main_ly)

        # Group Box content
        self.le_tag_data = QLineEdit()
        self.te_Script = QTextEdit()
        self.le_tag_data.setReadOnly(True)
        self.te_Script.setReadOnly(True)

        self.btn_get_checksum = QPushButton("Get Checksum")
        self.btn_clear = QPushButton("Clear")

        # Layout for the group box
        disp_data_ly = QVBoxLayout()
        io_data_ly = QHBoxLayout()

        disp_data_ly.addWidget(self.le_tag_data)
        disp_data_ly.addWidget(self.te_Script)
        # disp_data_ly.setSpacing(2)

        io_data_ly.addWidget(self.btn_get_checksum)
        io_data_ly.addWidget(self.btn_clear)

        main_ly.addLayout(disp_data_ly)
        main_ly.addLayout(io_data_ly)

