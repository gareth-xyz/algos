from stack import Stack
from linkedlist.doubly_linked_list import DoublyLinkedList

class ListStack(Stack):

    def __init__(self):
        self.list = DoublyLinkedList()
        self.iter_list = iter(self.list)