
from notifypy import Notify

def notify(title, message):
    notification = Notify()
    notification.title = title
    notification.message = message
    notification.send()
