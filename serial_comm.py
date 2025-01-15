import serial

class SerialComm:
    def __init__(self, port="COM1", baud_rate=9600):
        self.port = port
        self.baud_rate = baud_rate
        self.connection = None

    def open_connection(self):
        self.connection = serial.Serial(self.port, self.baud_rate)
        print("Serial connection opened.")

    def close_connection(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Serial connection closed.")

    def send_data(self, data):
        if self.connection and self.connection.is_open:
            self.connection.write(data.encode())
            print("Data sent.")