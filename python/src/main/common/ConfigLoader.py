import json
from pathlib import Path


class ConfigLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_config(self):
        with open(self.filepath, 'r') as config_file:
            return json.load(config_file)
