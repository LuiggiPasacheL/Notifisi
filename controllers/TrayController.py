
import pystray
from PIL import Image
from config import *
from controllers.NewsController import compare_and_notify_news, find_news

def create_stray(storage):
    domain = config['page']['domain']
    path = config['page']['path']
    image = Image.open('assets/logo.webp')

    def on_click(icon, item):
        if str(item) == "Open":
            print("hello")
        elif str(item) == "Reload":
            print("Realoading news")
            incoming_news = find_news(domain, path)
            compare_and_notify_news(storage, incoming_news)
        elif str(item) == "Exit":
            print("Closing")
            icon.stop()
        else:
            print("Feature not supported")

    icon = pystray.Icon("Notifisi", image, menu=pystray.Menu(
        pystray.MenuItem("Open", on_click),
        pystray.MenuItem("Reload", on_click),
        pystray.MenuItem("Exit", on_click)
    ))

    return icon
