from isp_unrefactored.components.log import Log
from isp_unrefactored.components.notification import Notification
from isp_unrefactored.db import DB
from isp_unrefactored.interfaces import RegisterInterface


class ContractModel(DB, RegisterInterface):

    def save(self):
        pass
