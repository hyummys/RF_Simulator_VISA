from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator
import datetime
from PyQt5.QtGui import QColor


class VisaTrxnSet(QGroupBox):
    def __init__(self, parent=None, main_window=None):
        super(VisaTrxnSet, self).__init__(parent)
        self.MainWindow = main_window
        #self.setTitle()

        gb_transaction = QGroupBox("Transaction")

        trxn_page_ly = QHBoxLayout()
        trxn_page_ly.addWidget(gb_transaction)
        #test_page_ly.addWidget(gb_log_window)

        transaction_ly = QGridLayout()

        gb_transaction.setLayout(transaction_ly)
       
        #Group Box 안에 들어갈 내용 작성
        self.le_amt = QLineEdit()
        self.cb_amt = QCheckBox("Amount")
        self.le_Transaction_Type = QLineEdit()
        self.cb_Transaction_Type = QCheckBox("Transaction Type")
        self.le_Transaction_Date = QLineEdit()
        self.cb_Transaction_Date = QCheckBox("Transaction Date")
        self.le_Transaction_Time = QLineEdit()
        self.cb_Transaction_Time = QCheckBox("Transaction Time")

        cur_date = datetime.datetime.now().strftime("%Y%m%d")
        cur_time = datetime.datetime.now().strftime("%H%M%S")

        self.le_Transaction_Date = QLineEdit(cur_date)
        self.le_Transaction_Time = QLineEdit(cur_time)
        
        trxn_line = 0
        transaction_ly.addWidget(self.cb_amt, trxn_line, 0)
        transaction_ly.addWidget(self.le_amt, trxn_line, 1)
        self.le_amt.setValidator(QIntValidator())
        self.le_amt.setMaxLength(12)
        # self.le_amt_auth.textChanged.connect(lambda: self.le_amt_auth.setText("0") if self.le_amt_auth.text() == "" else None)

        trxn_line += 1
        transaction_ly.addWidget(self.cb_Transaction_Type, trxn_line, 0)
        transaction_ly.addWidget(self.le_Transaction_Type, trxn_line, 1)
        self.le_Transaction_Type.setValidator(QIntValidator())
        self.le_Transaction_Type.setMaxLength(2)
        # self.le_trxn_type.textChanged.connect(lambda: self.le_trxn_type.setText("0") if self.le_trxn_type.text() == "" else None)

        trxn_line += 1
        transaction_ly.addWidget(self.cb_Transaction_Date, trxn_line, 0)
        transaction_ly.addWidget(self.le_Transaction_Date, trxn_line, 1)
        self.le_Transaction_Date.setValidator(QIntValidator())
        self.le_Transaction_Date.setMaxLength(8)
        
        trxn_line += 1
        transaction_ly.addWidget(self.cb_Transaction_Time, trxn_line, 0)
        transaction_ly.addWidget(self.le_Transaction_Time, trxn_line, 1)
        self.le_Transaction_Time.setValidator(QIntValidator())
        self.le_Transaction_Time.setMaxLength(6)


        transaction_ly.setRowStretch(transaction_ly.rowCount(), 1)

        self.setLayout(trxn_page_ly)
