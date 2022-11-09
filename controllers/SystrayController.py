
import pystray
from PIL import Image
from config import *
from controllers.NewsController import find_news, renew_and_notify_news
import os
import sys
import webbrowser

try:
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.abspath(".")
image_path = os.path.join(base_path, 'assets', 'logo.png')

def create_systray(storage):
    image = Image.open(image_path)

    def on_click(icon, item):
        if str(item) == "Abrir noticias":
            webbrowser.open(domain + path + '#tns1-item1')
        elif str(item) == "Recargar noticias":
            incoming_news = find_news(domain, path)
            renew_and_notify_news(storage, incoming_news)
        elif str(item) == "Salir":
            icon.stop()
        else:
            print("Feature not supported")

    icon = pystray.Icon("Notifisi", image, menu=pystray.Menu(
        pystray.MenuItem("Abrir noticias", on_click),
        pystray.MenuItem("Recargar noticias", on_click),
        pystray.MenuItem("Salir", on_click)
    ))

    return icon
