"""main.py"""
from ui_main import SimulatorUI
from serial_comm import SerialComm
from config_parser import ConfigParser

def main():
    config = ConfigParser("settings.ini").parse()
    serial_comm = SerialComm(port=config['COMM']['port'])
    app = SimulatorUI(serial_comm, config)
    app.run()

if __name__ == "__main__":
    main()

#etst#etst#etst#etst#etst#etst#etst
#etst