from abc import ABC, abstractmethod
class Stack(ABC):
    
    @abstractmethod
    def isEmpty(self):
        pass

    @abstractmethod
    def push(self, elem):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def size(self):
        pass
