class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.travIter = None

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
        if self.isEmpty():
            raise Exception('Empty list')
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        
        return data

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

    def __iter__(self): 
        """
        Called when iteration is initialized
        """
        self.travIter = self.head
        return self

    def __next__(self): 
        """
        To move to next element. 
        """
        # Stop iteration if limit is reached 
        if self.travIter is None:
            raise StopIteration
        
        # Store current travIter.data 
        data = self.travIter.data
        self.travIter = self.travIter.next
    
        # Else increment and return old value 
        return data

    def peek_last(self):
        """ 
        Check the value of the last node if it exists, O(1)
        """ 
        if self.is_empty():
            raise Exception('Empty list')
        return self.tail.data

    def peek_first(self):
        """ 
        Check the value of the last node if it exists, O(1)
        """ 
        if self.is_empty():
            raise Exception('Empty list')
        return self.head.data

class Node(object):
    def __init__(self, data, prev, next): 
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self.data)