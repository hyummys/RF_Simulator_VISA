import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget

class SimulatorUI:
    def __init__(self, serial_comm, config):
        self.serial_comm = serial_comm
        self.config = config

    def run(self):
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle("RF Simulator")
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        self.text_area = QTextEdit()
        layout.addWidget(self.text_area)
        
        connect_button = QPushButton("Open Serial")
        connect_button.clicked.connect(self.open_serial)
        layout.addWidget(connect_button)
        
        send_button = QPushButton("Send Test Data")
        send_button.clicked.connect(self.send_data)
        layout.addWidget(send_button)
        
        close_button = QPushButton("Close Serial")
        close_button.clicked.connect(self.close_serial)
        layout.addWidget(close_button)
        
        central_widget.setLayout(layout)
        window.setCentralWidget(central_widget)
        window.show()
        sys.exit(app.exec_())

    def open_serial(self):
        self.serial_comm.open_connection()
        self.text_area.append("Serial connection opened.")

    def send_data(self):
        data_str = "Test Data"
        self.serial_comm.send_data(data_str)
        self.text_area.append(f"Sent: {data_str}")

    def close_serial(self):
        self.serial_comm.close_connection()
        self.text_area.append("Serial connection closed.")