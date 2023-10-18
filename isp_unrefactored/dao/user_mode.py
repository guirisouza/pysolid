from isp_unrefactored.components.log import Log
from isp_unrefactored.components.notification import Notification
from isp_unrefactored.db import DB
from isp_unrefactored.interfaces import RegisterInterface, NotificationInterface, LogInterface


class UserModel(DB, RegisterInterface, NotificationInterface, LogInterface):
    def save(self):
        pass

    def log_register(self, log: Log):
        pass

    def send_notification(self, notification: Notification):
        pass