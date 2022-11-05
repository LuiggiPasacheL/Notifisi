
import pystray
from PIL import Image
from config import *
from controllers.NewsController import find_news, renew_and_notify_news

def create_stray(storage):
    domain = config['page']['domain']
    path = config['page']['path']
    image = Image.open('assets/logo.webp')

    def on_click(icon, item):
        if str(item) == "Recargar noticias":
            incoming_news = find_news(domain, path)
            renew_and_notify_news(storage, incoming_news)
        elif str(item) == "Salir":
            icon.stop()
        else:
            print("Feature not supported")

    icon = pystray.Icon("Notifisi", image, menu=pystray.Menu(
        pystray.MenuItem("Recargar noticias", on_click),
        pystray.MenuItem("Salir", on_click)
    ))

    return icon
