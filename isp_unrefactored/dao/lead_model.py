from isp_unrefactored.components.notification import Notification
from isp_unrefactored.db import DB
from isp_unrefactored.interfaces import NotificationInterface, RegisterInterface


class LeadModel(DB, NotificationInterface, RegisterInterface):
    def save(self):
        pass

    def send_notification(self, notification: Notification):
        pass