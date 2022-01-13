from abc import ABC, abstractmethod
class Queue(ABC):

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def offer(self, elem):
        pass

    @abstractmethod
    def poll(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass