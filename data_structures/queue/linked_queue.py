from queue import Queue
from doubly_linked_list import DoublyLinkedList

class LinkedQueue(Queue):

    def __init__(self):
        self.list = DoublyLinkedList()
        self.iter_list = iter(self.list)

    def size(self):
        return self.list.size()

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('Queue Empty')
        return self.list.peek_first()

    def poll(self):
        ''' poll from front of queue '''
        if self.isEmpty():
            raise Exception('Queue Empty')
        return self.list.remove_head()

    def offer(self, elem):
        ''' add elem to back of queue '''
        self.list.append(elem)

    def __iter__(self): 
        ''' called when iteration is initialized '''
        self.iter_list = iter(self.list)
        return self

    def __next__(self): 
        ''' To move to next element '''
        return next(self.iter_list)

if __name__ == '__main__':
    q = LinkedQueue()
    q.offer(1)
    q.offer(2)
    q.offer(3)
    q.offer(4)
    q.offer(5)

    print(q.poll()) # 1
    print(q.poll()) # 2
    print(q.poll()) # 3
    print(q.poll()) # 4

    print(q.isEmpty()) # false

    q.offer(1)
    q.offer(2)
    q.offer(3)

    print(q.poll()) # 5
    print(q.poll()) # 1
    print(q.poll()) # 2
    print(q.poll()) # 3

    print(q.isEmpty()) # true


    