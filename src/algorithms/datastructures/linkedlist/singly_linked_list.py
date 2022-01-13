class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def size(self):
        return self.size

    def is_empty(self):
        return self.size() == 0

    def append(self, elem):
        # append O(n)
        node = Node(elem, None)
        if self.is_empty():
            self.head = node
        else:
            # traverse the list to find tail, and append
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = node
        self.size += 1

    def add_head(self, elem):
        # O(1)
        if self.is_empty():
            self.head = Node(elem, None)
        else:
            node = Node(elem, self.head)
            self.head = node
        self.size += 1

    def remove_head(self):
        # O(1)
        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        self.size -= 1

    def remove_tail(self, node):
        # O(n)
        if self.is_empty():
            raise Exception('empty')
        else:
            # traverse the list to find tail, and remove
            trav = self.head
            prev = None
            while trav.next is not None:
                prev = trav
                trav = trav.next    
            if prev:
                prev.next = None
            else:
                self.head = None
        self.size -= 1

    def clear(self):
        # O(n)
        trav = self.head
        while trav is not None:
            next = trav.next
            trav.data = None
            trav.next = None
            trav = next
        self.head = None
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
    def __init__(self, data, next):
        self.data  = val
        self.next = next