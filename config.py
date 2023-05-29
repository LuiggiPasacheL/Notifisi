import json
import sys
import os

class Config:

    def __init__(self):
        self.dir_name = self.__create_dir_if_no_exists()
        self.config_path = os.path.join(self.dir_name, "config.json")
        self.base_path = self.__get_base_path()
        self.image_path = os.path.join(self.base_path, 'assets', 'logo.png')
        self.load()

    def load(self):
        try:
            with open(self.config_path, 'r') as f:
                config_file = json.load(f)
            self.domain = config_file["page"]["domain"]
            self.path = config_file["page"]["path"]
            self.url = self.domain + self.path
            self.displayed_news = self.__get_displayed_news(int(config_file['displayed_news']))
            self.data_path = os.path.join(self.dir_name, config_file["file_name"] + ".json")
            self.queryselectors = {
                "cards": config_file["page"]["queryselectors"]["cards"],
                "titles": config_file["page"]["queryselectors"]["titles"],
                "descriptions": config_file["page"]["queryselectors"]["descriptions"],
                "links": config_file["page"]["queryselectors"]["links"],
            }
        except:
            self.save()

    def save(self):
        with open(self.config_path, 'w') as f:
            json.dump( {
                "page": {
                    "domain": "https://sistemas.unmsm.edu.pe",
                    "path": "/site/index.php",
                    "queryselectors": {
                        "cards": ".mfp_carousel_item,.tns-item,.tns-slide-active",
                        "titles": "h4.mfp_carousel_title",
                        "descriptions": "p.mfp_carousel_introtext",
                        "links": "h4.mfp_carousel_title>a",
                    },
                },
                "displayed_news": 5,
                "file_name": "data",
            } , f, indent=True)

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
        if quantity < 0:
            return 0
        elif quantity > 15:
            return 15
        else:
            return quantity

