from abc import ABC, abstractmethod


class MessageInterface(ABC):

    @abstractmethod
    def send(self):
        pass