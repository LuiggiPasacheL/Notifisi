
from notifypy import Notify
notification = Notify()

def notify(title, message):
    notification.title = title
    notification.message = message
    notification.send()
