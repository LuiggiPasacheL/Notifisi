
import pystray
from PIL import Image
import config
from controllers.NewsController import find_news, renew_and_notify_news
import webbrowser


def create_systray(storage):
    image = Image.open(config.image_path)

    def on_click(icon, item):
        if str(item) == "Abrir noticias":
            webbrowser.open(config.domain + config.path + '#tns1-item1')
        elif str(item) == "Recargar noticias":
            incoming_news = find_news(config.domain, config.path)
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
