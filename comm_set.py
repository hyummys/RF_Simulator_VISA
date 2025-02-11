import time
from PyQt5.QtWidgets import *
import serial.tools.list_ports
import serial
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
import serial.serialutil

class SerialReader(QThread):
    data_received = pyqtSignal(list)
    data_received_raw = pyqtSignal()  # 타이머 초기화를 위한 신호

    def __init__(self, serial_port, buffer_size=1024*4):
        super().__init__()
        self.serial_port = serial_port
        self.is_running = True
        self.buffer_size = buffer_size

    def run(self):
        while self.is_running:
            if self.serial_port and self.serial_port.isOpen():
                try:
                    data = self.serial_port.read(self.buffer_size)
                    if data:
                        hex_data = [f'0x{item:02x}' for item in data]
                        self.data_received.emit(hex_data)
                        self.data_received_raw.emit()  # 타이머 초기화를 위한 신호 발생
                except (TypeError, AttributeError, serial.serialutil.SerialException) as e:
                    print("Error: ", e)
                    self.serial_port.close()  # Close the serial port if an error occurs

    def stop(self):
        self.is_running = False

class CommSet(QGroupBox):
    TIMER_INTERVAL = 100  # 타이머 시간을 변수로 지정

    def __init__(self, parent=None, main_window=None):
        super(CommSet, self).__init__(parent)
        self.MainWindow = main_window
        self.setTitle('[Set Comm]')

        self.ser = None

        # Group Box content
        self.cb_comm_list = QComboBox()
        
        ports = serial.tools.list_ports.comports()
        for port in ports:
            self.cb_comm_list.addItem(port.device)

        self.btn_open_comm = QPushButton("Open")
        self.btn_open_comm.clicked.connect(lambda: self.disconnect_to_serial() if self.btn_open_comm.text() == "Close" else self.connect_to_serial())

        comm_btn_size = 100
        self.cb_comm_list.setFixedWidth(comm_btn_size)
        self.btn_open_comm.setFixedWidth(comm_btn_size)

        self.le_comm_status = QLineEdit("Select Comm Port and Click Open")
        self.le_comm_status.setReadOnly(True)

        # Layout for the group box
        layout = QHBoxLayout()
        layout.addWidget(self.cb_comm_list)
        layout.addWidget(self.btn_open_comm)
        layout.addWidget(self.le_comm_status)
        self.setLayout(layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.flush_buffer)
        self.buffer = []

    def connect_to_serial(self):
        try:
            self.ser = serial.Serial(self.cb_comm_list.currentText(), 115200, timeout=0.1)

            if self.ser.isOpen():
                self.le_comm_status.setText("Connected to " + self.cb_comm_list.currentText())
                #change button text to close
                self.btn_open_comm.setText("Close")
                self.serial_reader = SerialReader(self.ser)
                self.serial_reader.data_received.connect(self.on_data_received)
                self.serial_reader.data_received_raw.connect(self.reset_timer)  # 타이머 초기화 신호 연결
                self.serial_reader.start()
                self.timer.start(self.TIMER_INTERVAL)  # Start the timer with the specified interval
            else:
                self.le_comm_status.setText("Disconnected")
        except serial.serialutil.SerialException:            
            print("Serial Exception")
            self.le_comm_status.setText("Already Opened")
    
    def disconnect_to_serial(self):
        try:
            self.ser.close()
            self.le_comm_status.setText("Disconnected")
            
            self.btn_open_comm.setText("Open")
            if self.serial_reader and self.serial_reader.isRunning():
                self.serial_reader.stop()
                self.serial_reader.wait()
            self.timer.stop()
        except serial.serialutil.SerialException:
            print("Serial Exception")
            self.le_comm_status.setText("Already Closed")

    def on_data_received(self, data):
        self.buffer.extend(data)

    def reset_timer(self):
        self.timer.start(self.TIMER_INTERVAL)  # Reset the timer on data reception

    def flush_buffer(self):
        if self.buffer:
            self.buffer = []

class TypeSet(QGroupBox):
    def __init__(self, parent=None, main_window=None):
        super(TypeSet, self).__init__(parent)
        self.MainWindow = main_window
        self.setTitle('[Type]')

        # Group Box content
        self.rb_TF = QRadioButton("TF")
        self.rb_TC= QRadioButton("TC")
        self.rb_TP = QRadioButton("TP")
        self.rb_TF.setChecked(True)

        # Layout for the group box
        layout = QHBoxLayout()
        layout.addWidget(self.rb_TF)
        layout.addWidget(self.rb_TC)
        layout.addWidget(self.rb_TP)
        self.setLayout(layout)
        