
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)

# >>> n = Node(5)
# >>> p = Node(6)
# >>> q = Node(7)
# >>> n.add_child(p)
# >>> n.add_child(q)