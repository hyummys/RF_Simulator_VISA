import configparser

class ConfigParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        config = configparser.ConfigParser()
        config.read(self.filepath)
        return config