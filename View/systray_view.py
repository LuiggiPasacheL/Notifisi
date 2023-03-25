
from PIL import Image
import webbrowser
import pystray
import threading
from config import Config

class SystrayView:

    def __init__(self) -> None:
        self.conf = Config()
        self.image = Image.open(self.conf.image_path)
        self.icon = pystray.Icon("Notifisi", self.image)

    def create_menu(self, controller):
        self.icon.menu = pystray.Menu(
            pystray.MenuItem("Abrir Noticias", 
                lambda _ : webbrowser.open(self.conf.url + '#tns1-item1')),
            pystray.MenuItem("Recargar Noticias", 
                             lambda _ : controller.update_news()),
            pystray.MenuItem("Salir", 
                lambda _ : self.icon.stop())
        )

    def update_menu(self, news_list):
        # TODO: Implement
        # def update():
        #     self.menu.clear()
        #     for news in news_list:
        #         self.icon.menu.append(news.title, None)
        # thread = threading.Thread(target=update)
        # thread.start()
        pass

    def run(self):
        def execute_systray():
            self.icon.run()
        thread = threading.Thread(target=execute_systray)
        thread.start()
