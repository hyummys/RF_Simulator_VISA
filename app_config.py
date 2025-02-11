import os
from PyQt5.QtWidgets import *
import sys
import configparser

class VISA_FileConfig(QGroupBox):
    def __init__(self, parent=None, main_window=None):
        super(VISA_FileConfig, self).__init__(parent)
        self.MainWindow = main_window
        self.setTitle('[VISA Config]')

        # Initialize layout
        main_ly = QVBoxLayout()

        # Create dropdown & button horizontally
        self.comboBox = QComboBox()
        self.comboBox.setMinimumWidth(200)
        self.items = self.load_packet_ini('packet.ini')
        self.comboBox.addItems(self.items)
        self.comboBox.currentIndexChanged.connect(self.handle_dropdown_selection)

        self.btn_packet_manager = QPushButton('...')
        self.btn_packet_manager.setFixedWidth(50)
        self.btn_packet_manager.clicked.connect(self.open_packet_manager)

        h_widget = QWidget()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.comboBox)
        h_layout.addWidget(self.btn_packet_manager)
        h_widget.setLayout(h_layout)
        main_ly.addWidget(h_widget)

        # Replace 'CONFIG' label with 'Configuration' button
        config_btn_widget = QWidget()
        box_layout = QVBoxLayout()
        self.config_button = QPushButton('Configuration')
        self.config_button.clicked.connect(self.open_pw_config)
        box_layout.addWidget(self.config_button)
        config_btn_widget.setLayout(box_layout)

        main_ly.addWidget(config_btn_widget)
        self.setLayout(main_ly)

    def load_packet_ini(self, filepath):
        config = configparser.ConfigParser()
        config.read(filepath)
        items = []
        for section in sorted(config.sections()):
            label = config[section]['LABEL']
            items.append(f"{section}-{label}")
        return items

    def handle_dropdown_selection(self):
        selected_text = self.comboBox.currentText()
        # Handle selection change if needed

    def open_packet_manager(self):
        self.packet_manager = PacketManager(self)
        self.packet_manager.exec_()
        self.items = self.load_packet_ini('packet.ini')
        self.comboBox.clear()
        self.comboBox.addItems(self.items)

    def open_pw_config(self):
        self.pw_config = PWConfigDialog(self)
        self.pw_config.exec_() 

class PacketManager(QDialog):
    def __init__(self, parent=None):
        super(PacketManager, self).__init__(parent)
        self.setWindowTitle("Packet Manager")
        self.setGeometry(100, 100, 600, 400)

        self.config = configparser.ConfigParser()
        self.config.read('packet.ini')

        main_layout = QHBoxLayout()

        # Left side: Packet selection
        self.packet_list = QListWidget()
        self.packet_list.addItems([f"{section}-{self.config[section]['LABEL']}" for section in sorted(self.config.sections())])
        self.packet_list.currentItemChanged.connect(self.load_packet_details)
        main_layout.addWidget(self.packet_list)

        # Right side: Packet details
        details_layout = QVBoxLayout()

        index_layout = QHBoxLayout()
        self.index_label = QLabel("Index:")
        self.index_field = QLineEdit()
        index_layout.addWidget(self.index_label)
        index_layout.addWidget(self.index_field)

        label_layout = QHBoxLayout()
        self.label_label = QLabel("Label:")
        self.label_field = QLineEdit()
        label_layout.addWidget(self.label_label)
        label_layout.addWidget(self.label_field)


        data_layout = QHBoxLayout()
        self.data_label = QLabel("Data:")
        self.data_field = QTextEdit()
        data_layout.addWidget(self.data_label)
        data_layout.addWidget(self.data_field)


        ioBtn_layout = QHBoxLayout()
        self.write_button = QPushButton("Write")
        self.write_button.clicked.connect(self.write_packet)
        self.remove_button = QPushButton("Remove")
        self.remove_button.clicked.connect(self.remove_packet)
        ioBtn_layout.addWidget(self.write_button)
        ioBtn_layout.addWidget(self.remove_button)


        # Bottom: Confirm/Cancel buttons
        button_layout = QHBoxLayout()
        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.confirm)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel)
        button_layout.addWidget(self.confirm_button)
        # button_layout.addWidget(self.cancel_button)

        
        details_layout.addLayout(index_layout)
        details_layout.addLayout(label_layout)
        details_layout.addLayout(data_layout)
        details_layout.addLayout(ioBtn_layout)
        details_layout.addLayout(button_layout)
        
        main_layout.addLayout(details_layout)

        self.setLayout(main_layout)

    def load_packet_details(self, current, previous):
        if current:
            index = current.text().split('-')[0]
            self.index_field.setText(index)
            try:
                self.label_field.setText(self.config[index]['LABEL'])
                self.data_field.setText(self.config[index]['DATA'])
            except KeyError:
                self.label_field.setText("")
                self.data_field.setText("")

    def write_packet(self):
        index = self.index_field.text().zfill(4)
        label = self.label_field.text()
        data = self.data_field.text()
        self.config[index] = {'LABEL': label, 'DATA': data}
        with open('packet.ini', 'w', encoding='UTF8') as configfile:
            self.config.write(configfile)
        self.packet_list.clear()
        self.packet_list.addItems([f"{section}-{self.config[section]['LABEL']}" for section in sorted(self.config.sections())])

    def remove_packet(self):
        index = self.index_field.text().zfill(4)
        self.config.remove_section(index)
        with open('packet.ini', 'w', encoding='UTF8') as configfile:
            self.config.write(configfile)
        self.packet_list.clear()
        self.packet_list.addItems([f"{section}-{self.config[section]['LABEL']}" for section in sorted(self.config.sections())])

    def confirm(self):
        with open('packet.ini', 'w', encoding='UTF8') as configfile:
            self.config.write(configfile)
        self.accept()

    def cancel(self):
        self.reject()



class PWConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(PWConfigDialog, self).__init__(parent)
        self.setWindowTitle("PW Config")
        self.setGeometry(100, 100, 800, 600)

        main_layout = QVBoxLayout()

        # Left side: Config file selection
        left_layout = QVBoxLayout()
        self.config_list = QListWidget()
        self.load_config_files()
        self.config_list.currentItemChanged.connect(self.load_config_details)
        left_layout.addWidget(self.config_list)

        self.file_name_label = QLabel("File Name:")
        self.file_name_field = QLineEdit()
        left_layout.addWidget(self.file_name_label)
        left_layout.addWidget(self.file_name_field)

        self.config_dropdown = QComboBox()
        left_layout.addWidget(self.config_dropdown)

        self.save_button = QPushButton("Save Parameters")
        self.save_button.clicked.connect(self.save_parameters)
        left_layout.addWidget(self.save_button)

        self.download_button = QPushButton("Download Parameters")
        left_layout.addWidget(self.download_button)

        main_layout.addLayout(left_layout)

        # Right side: Config parameters
        self.param_layout = QVBoxLayout()
        self.param_scroll = QScrollArea()
        self.param_widget = QWidget()
        self.param_widget.setLayout(self.param_layout)
        self.param_scroll.setWidget(self.param_widget)
        self.param_scroll.setWidgetResizable(True)
        main_layout.addWidget(self.param_scroll)

        self.setLayout(main_layout)

    def load_config_files(self):
        config_files = [f for f in os.listdir('./cfg') if f.endswith('.ini')]
        self.config_list.addItems(config_files)

    def load_config_details(self, current, previous):
        if current:
            file_name = current.text()
            self.file_name_field.setText(file_name)
            config = configparser.ConfigParser()
            config.read(f'./cfg/{file_name}')
            self.param_layout = QVBoxLayout()
            for section in config.sections():
                for key, value in config.items(section):
                    h_layout = QHBoxLayout()
                    checkbox = QCheckBox(key)
                    lineedit = QLineEdit(value)
                    h_layout.addWidget(checkbox)
                    h_layout.addWidget(lineedit)
                    self.param_layout.addLayout(h_layout)
            self.param_widget.setLayout(self.param_layout)

    def save_parameters(self):
        file_name = self.file_name_field.text()
        config = configparser.ConfigParser()
        for i in range(self.param_layout.count()):
            h_layout = self.param_layout.itemAt(i).layout()
            key = h_layout.itemAt(0).widget().text()
            value = h_layout.itemAt(1).widget().text()
            section = 'DEFAULT'
            if not config.has_section(section):
                config.add_section(section)
            config.set(section, key, value)
        with open(f'./cfg/{file_name}', 'w', encoding='UTF8') as configfile:
            config.write(configfile)