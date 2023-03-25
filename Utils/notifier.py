
from config import Config
from notifypy import Notify

conf = Config()
notification = Notify(
    default_notification_application_name='Notifisi', 
    default_notification_icon=conf.image_path
)

def notify(title, message):
    notification.title = title
    notification.message = message
    notification.icon = conf.image_path
    notification.send()

def notify_news(diff):
    if diff > 0:
        notify("Se encontraron noticias", f"{diff} noticias encontradas")
    else:
        notify("No se encontraron noticias", "")

def notify_error(error):
    notify("Ha ocurrido un error", error)
