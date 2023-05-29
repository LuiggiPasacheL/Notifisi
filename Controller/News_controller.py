from Model.Storage import Storage
from Utils.notifier import notify_error, notify_news
from View.systray_view import SystrayView
import os
import sys

class NewsController:

    def __init__(self, view: SystrayView, model: Storage) -> None:
        self.model = model
        self.view = view

    def get_news(self):
        return self.model.news
    
    def open_config(self):
        path = self.model.conf.config_path
        if sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
            os.system('open ' + path)
        elif sys.platform.startswith('win'):
            os.system('start ' + path)
        else:
            raise Exception("No se puede abrir en este sistema operativo")

    def update_news(self, auto=False):
        try:
            self.model.conf.load()
            diff = self.model.update_news()
            self.model.save_news()
            if auto == False:
                notify_news(diff)
            elif diff > 0:
                notify_news(diff)
            self.view.update_menu(self)
        except Exception as e:
            notify_error(str(e))

    def run(self):
        self.view.create_menu(self)
        self.view.run()
