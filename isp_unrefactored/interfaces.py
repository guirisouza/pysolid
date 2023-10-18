from abc import ABC, abstractmethod
from isp_unrefactored.components.log import Log
from isp_unrefactored.components.notification import Notification


class RegisterInterface(ABC):

    @abstractmethod
    def save(self):
        pass


class LogInterface(ABC):
    @abstractmethod
    def log_register(self, log: Log):
        pass


class NotificationInterface(ABC):
    @abstractmethod
    def send_notification(self, notification: Notification):
        pass