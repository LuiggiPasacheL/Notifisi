import json
import sys
import os
from datetime import datetime

class Config:

    def __init__(self):
        self.config_path = os.path.join("config.json")
        self.current_time = datetime.now().strftime("%H:%M")
        try:
            self.base_path = sys._MEIPASS
        except Exception:
            self.base_path = os.path.abspath(".")
        self.image_path = os.path.join(self.base_path, 'assets', 'logo.png')
        self.load()

    def load(self):
        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
        except:
            self.save()
            with open(self.config_path, 'r') as f:
                data = json.load(f)
        self.domain = data["page"]["domain"]
        self.path = data["page"]["path"]
        self.url = self.domain + self.path
        self.data_path = os.path.join("data", data["file_name"] + ".json")
        self.time = data['time']

    def save(self):
        with open(self.config_path, 'w') as f:
            json.dump( {
                "page": {
                    "domain": "https://sistemas.unmsm.edu.pe",
                    "path": "/site/index.php"
                },
                "file_name": "data",
                "time": self.current_time
            } , f)
