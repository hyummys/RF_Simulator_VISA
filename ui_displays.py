from PyQt5.QtWidgets import *

class VisaDataWindows(QVBoxLayout):
    def __init__(self, parent=None, main_window=None):
        super(VisaDataWindows, self).__init__(parent)
        self.MainWindow = main_window
        
        layout_datainfo1 = QHBoxLayout()
        layout_datainfo2 = QHBoxLayout()
        layout_datainfo3 = QHBoxLayout()

        self.te_datainfo1 = QTextEdit()
        self.te_datainfo2 = QTextEdit()
        self.te_datainfo3 = QTextEdit()
        self.te_datainfo3.setReadOnly(True)

        self.btn_clear_window = QPushButton("Clear")
        self.btn_clear_window.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)


        layout_datainfo1.addWidget(self.te_datainfo1)
        self.addLayout(layout_datainfo1, 6)

        layout_datainfo2.addWidget(self.te_datainfo2)
        self.addLayout(layout_datainfo2, 1)

        layout_datainfo3.addWidget(self.te_datainfo3, 9)
        layout_datainfo3.addWidget(self.btn_clear_window, 1)
        self.addLayout(layout_datainfo3, 3)