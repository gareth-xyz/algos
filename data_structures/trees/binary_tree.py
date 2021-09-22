"""
Python Binary Tree representation

Supports:
    Search
    Insert
    Delete
    Traversal
        DFS - pre/in/post order
        BFS - level order
"""
from collections import deque
from enum import Enum, auto

class Node:
    def __init__( self, val, left = None, right = None ):
        self.val = val
        self.left = left
        self.right = right


class TreeTraversalOrder(Enum):
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()
    LEVEL_ORDER = auto()


class BinaryTree:
    """ 
    Binary tree representation
    
    Attributes:
        root: the root node of the tree
    """

    def __init__(self, root = None):
        """ inits BinaryTree class, with the option of a root node """
        self.root = root

    def insert(self, elem):
        """ inserts a node or element into the tree """

        if self.root is None:
            if isinstance(item, Node):
                self.root = elem
            else:
                self.root = Node(elem)

    def delete(self, root, elem):
        """ removes an element from the tree - replaces with bottom-right most node """
        if self.search(root, elem):
            # perform delete
            pass
        else:
            return False

    def search(self, root, elem):
        """ searches for the element in the tree by checking each node's val attribute """
        if root is None:
            return False
        
        if root.val == elem:
            return True

        self.search(root.left, elem)
        self.search(root.right, elem)

    def traverse(self, root, traverse_type):
        """ traverses the tree by the given type """
        if traverse_type = TreeTraversalOrder.PRE_ORDER:
            return self._pre_order_traversal(root)
        if traverse_type = TreeTraversalOrder.IN_ORDER:
            return self._in_order_traversal(root)
        if traverse_type = TreeTraversalOrder.POST_ORDER:
            return self._post_order_traversal(root)
        if traverse_type = TreeTraversalOrder.LEVEL_ORDER:
            return self._level_order_traversal(root)

    def _pre_order_traversal(self, root):
        """ performs pre-order traversal, root>left>right """
        if root is None:
            return False
        else:
            print(root.val)
            self._pre_order_traversal(root.left)
            self._pre_order_traversal(root.right)

    def _in_order_traversal(self, root):
        """ performs in-order traversal, left>root>right """
        if root is None:
            return False
        else:
            self._pre_order_traversal(root.left)
            print(root.val)
            self._pre_order_traversal(root.right)

    def _post_order_traversal(self, root):
        """ performs post-order traversal, right>left>root """
        if root is None:
            return False
        else:
            self._pre_order_traversal(root.left)
            self._pre_order_traversal(root.right)
            print(root.val)

    def _level_order_traversal(self, root):
        """ traverses the tree level by level """
        if root is None:
            return

        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            
            node = queue.popleft()
            print(node.val)

            if node.left is not None:
                queue.append(node.left)    

            if node.right is not None:
                queue.append(node.right)


def main():
    binary_tree = BinaryTree()


if __name__ == '__main__':
    main()
