class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def size(self):
        return self.size

    def is_empty(self):
        return self.size() == 0

    def append(self, elem):
        # append O(1)
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            node = Node(elem, self.tail, None)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def add_head(self, elem):
        # O(1)
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            node = Node(elem, None, self.head)
            self.head.prev = node
            self.head = node
        self.size += 1

    def remove_head(self):
        # O(1)
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None
        self.size -= 1

    def remove_tail(self, node):
        # O(1)
        if self.is_empty():
            raise Exception('empty')
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data

    def clear(self):
        # O(n)
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next
        self.head = None
        self.tail = None
        trav = None
        self.size = 0

    def contains(self, obj):
        # O(n)
        return self.index_of(obj) != -1

    def index_of(self, obj):
        # O(n)
        index = 0
        trav  = self.head
        while trav is not None:
            if obj == trav.data:
                return index
            trav = trav.next
            index += 1

        return -1

class Node:
    def __init__(self):
        self.prev = None
        self.next = None