
from PIL import Image
import webbrowser
import pystray
import threading
from config import Config

class SystrayView:

    def __init__(self, config: Config) -> None:
        self.conf = config
        self.image = Image.open(self.conf.image_path)
        self.icon = pystray.Icon("Notifisi", self.image)

    def create_menu(self, controller):
        news_list = controller.get_news()
        
        def create_menu_item(news_item):
            def open_link():
                news_item.open_link()
            return lambda _ : open_link()

        news_menu_items = [ pystray.MenuItem(news.get_short_title(), create_menu_item(news)) for news in news_list[:self.conf.displayed_news] ]

        self.icon.menu = pystray.Menu(
            pystray.MenuItem("Abrir Noticias", lambda _ : webbrowser.open(self.conf.url)),
            pystray.MenuItem("Noticias", pystray.Menu(*news_menu_items)),
            pystray.MenuItem("Recargar Noticias", lambda _ : controller.update_news()),
            pystray.MenuItem("Abrir configuración", lambda _ : controller.open_config()),
            pystray.MenuItem("Salir", lambda _ : self.icon.stop())
        )

    def update_menu(self, controller):
        self.create_menu(controller)
        self.icon.update_menu()

    def run(self):
        def execute_systray():
            self.icon.run()
        thread = threading.Thread(target=execute_systray)
        thread.start()
