
import pystray
from PIL import Image

image = Image.open('assets/logo.webp')

def on_click(icon, item):
    if str(item) == "Open":
        print("hello")
    elif str(item) == "Exit":
        print("Close")
        icon.stop()
        exit()

icon = pystray.Icon("Notifisi", image, menu=pystray.Menu(
    pystray.MenuItem("Open", on_click),
    pystray.MenuItem("Exit", on_click)
))
