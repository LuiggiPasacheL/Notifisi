import json
import sys
import os

class Config:

    def __init__(self):
        self.dir_name = self.__create_dir_if_no_exists()
        self.config_path = os.path.join(self.dir_name, "config.json")
        self.base_path = self.__get_base_path()
        self.image_path = os.path.join(self.base_path, 'assets', 'logo.png')
        self.domain = "https://sistemas.unmsm.edu.pe"
        self.path = "/site/index.php"
        self.url = self.domain + self.path
        self.load()

    def load(self):
        try:
            with open(self.config_path, 'r') as f:
                data = json.load(f)
            self.displayed_news = self.__get_displayed_news(int(data['displayed_news']))
            self.data_path = os.path.join(self.dir_name, data["file_name"] + ".json")
        except:
            self.save()
            with open(self.config_path, 'r') as f:
                data = json.load(f)

    def save(self):
        with open(self.config_path, 'w') as f:
            json.dump( {
                "displayed_news": 5,
                "file_name": "data",
            } , f)

    def __create_dir_if_no_exists(self):
        dir_name = "resources"
        if not os.path.exists(dir_name):
            dir_path = os.path.join(dir_name)
            os.mkdir(dir_path)
        return dir_name
    
    def __get_base_path(self):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return base_path

    def __get_displayed_news(self, quantity: int):
        if quantity <= 0:
            return 1
        elif quantity > 15:
            return 15
        else:
            return quantity

