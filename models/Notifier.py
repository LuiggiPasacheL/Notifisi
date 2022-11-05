
import os
import sys
from notifypy import Notify

try:
    base_path = sys._MEIPASS
except Exception:
    base_path = os.path.abspath(".")

notification = Notify(
    default_notification_application_name='Notifisi', 
    default_notification_icon=os.path.join(base_path, 'assets', 'logo.png')
)

def notify(title, message):
    notification.title = title
    notification.message = message
    notification.icon = os.path.join(base_path, 'assets', 'logo.png')
    notification.send()
