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
            self.root = Node(elem)
        else:
            queue = deque()
            queue.append(self.root)

            while len(queue):
                temp = queue.popleft()

                if not temp.left:
                    temp.left = Node(elem)
                    break
                if not temp.right:
                    temp.right = Node(elem)
                    break
                queue.append(temp.left)
                queue.append(temp.right)

    def delete(self, elem):
        """ removes an element from the tree - replaces with bottom-right most node """
        if self.search(elem):
            queue = deque()
            queue.append(self.root)

            while len(queue)>0:
                temp = queue.popleft()

                if temp.val == elem:
                    target = temp

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            target.val = temp.val
            # delete deepest/right most
            print('----in delete')
            print(temp)
            self.delete_deepest(temp)
            return True
        else:
            return False

    def _delete_deepest(self, del_node):
        """ deletes the deepest, right most node """
        queue = deque()
        queue.append(self.root)

        while len(queue):
            temp = queue.popleft()

            if temp.left == del_node:
                temp.left = None
                return
            else:
                queue.append(temp.left)

            if temp.right == del_node:
                temp.right = None
                return
            else:
                queue.append(temp.right)

    def search(self, elem):
        """ public function to search for an element in the tree """
        return self._search(self.root, elem)

    def _search(self, root, elem):
        """ searches for the element in the tree by checking each node's val attribute """
        if root is None:
            return False
        
        if root.val == elem:
            return True
        else:
            self._search(root.left, elem)
            self._search(root.right, elem)

    def traverse(self, traverse_type):
        """ traverses the tree by the given type """
        if traverse_type == TreeTraversalOrder.PRE_ORDER:
            return self._pre_order_traversal(self.root)
        if traverse_type == TreeTraversalOrder.IN_ORDER:
            return self._in_order_traversal(self.root)
        if traverse_type == TreeTraversalOrder.POST_ORDER:
            return self._post_order_traversal(self.root)
        if traverse_type == TreeTraversalOrder.LEVEL_ORDER:
            return self._level_order_traversal(self.root)

    def _pre_order_traversal(self, root):
        """ performs pre-order traversal, root>left>right """
        if root is None:
            return
        else:
            print(root.val)
            self._pre_order_traversal(root.left)
            self._pre_order_traversal(root.right)

    def _in_order_traversal(self, root):
        """ performs in-order traversal, left>root>right """
        if root is None:
            return
        else:
            self._pre_order_traversal(root.left)
            print(root.val)
            self._pre_order_traversal(root.right)

    def _post_order_traversal(self, root):
        """ performs post-order traversal, right>left>root """
        if root is None:
            return
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

            if node.left:
                queue.append(node.left)    

            if node.right:
                queue.append(node.right)


def main():
    binary_tree = BinaryTree()
    binary_tree.root = Node(1)
    binary_tree.root.left = Node(2)
    binary_tree.root.right = Node(3)
    binary_tree.root.left.left = Node(4)
    binary_tree.root.left.right = Node(5)
    binary_tree.root.right.left = Node(6)
    binary_tree.root.right.right = Node(7)
    binary_tree.traverse( TreeTraversalOrder.LEVEL_ORDER )
    print(binary_tree.search(7))
    print('*********** insert ')
    binary_tree.insert(8)
    binary_tree.traverse( TreeTraversalOrder.LEVEL_ORDER )
    print('*********** delete')
    binary_tree.delete(8)
    binary_tree.traverse( TreeTraversalOrder.LEVEL_ORDER )

if __name__ == '__main__':
    main()
