import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from ui_main import Ui_MainWindow
import time

# Program Version
MAJOR_VER_NUM = '1'
MINOR_VER_NUM = '057'
PROGRAM_VER = MAJOR_VER_NUM + '.' + MINOR_VER_NUM

# Program Date to current date in YYMMDD format
PROGRAM_DATE = time.strftime("%y%m%d")

# Program Title
PROGRAM_TITLE = "NICE RF Host Emulator"

PROGRAM_NAME = PROGRAM_TITLE + " V" + PROGRAM_VER  + " (" + PROGRAM_DATE + ")"

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle(PROGRAM_NAME)
        self.setWindowIcon(QIcon('./nice_ci.jpg'))
        self.move(300, 100)

        self.setupUI(self)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
