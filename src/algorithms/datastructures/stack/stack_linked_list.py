from stack import Stack
from data_structures.linkedlist.doubly_linked_list import DoublyLinkedList

class ListStack(Stack):

    def __init__(self):
        self.list = DoublyLinkedList()
        self.iter_list = iter(self.list)

    def size(self):
        return self.list.size()

    def is_empty(self):
        return self.size() == 0

    def push(self, elem):
        self.list.append(elem)

    def pop(self):
        if self.is_empty():
            raise Exception('empty stack')
        return self.list.remove_tail()

    def peek(self):
        if self.is_empty():
            raise Exception('empty stack')
        return self.list.tail
    
    def __iter__(self): 
        self.iter_list = iter(self.list)
        return self

    def __next__(self): 
        return next(self.iter_list)

    