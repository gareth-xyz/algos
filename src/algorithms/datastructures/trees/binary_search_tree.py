"""
Python Binary Search Tree representation

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


class BinarySearchTree:
    """
    Binary search tree representation
    
    Attributes:
        root: the root node of the tree
    """
    def __init__(self, root = None):
        """ inits BinarySearchTree class with optional root node """
        self.root = root

    def insert(self, elem):
        """ inserts an element into the tree, returns True if successful """
        if self.search(elem):
            return False
        
        self.root = self._insert(self.root, elem)
        return True

    def _insert(self, node, elem):
        """ recursive private method to insert into the tree """
        if node == None:
            node = Node(None, None, elem)
        
        else:
            if elem < node.val:
                node.left = self._insert(node.left, elem)
            else:
                node.right = self._insert(node.right, elem)

        return node

    def delete(self, elem):
        """ removes an element from the tree if it exists, returns True if successful """
        if self.search(elem):
            self.root = self._delete(self.root, elem)
            return True
        else:
            return False

    def _delete(self, node, elem):
        """ recursive private method to delete an element from the tree """
        if node == None:
            return
        # Cases:
            # 1 remove leaf node - simply remove
            # 2 remove a node with one child - replace with left/right node
            # 3 remove a node with 2 children - replace with either largest in left/smallest in right
                # if left:  go as far right as possible in left child
                # if right: go as far left as possible in right child
        
        if elem == node.data:
            
            # case 1 or 2
            if not node.left:
                right_child = node.right
                node.val = None
                node = None
                return right_child

            # case 2
            elif not node.right:
                left_child = node.left
                node.val = None
                node = None
                return left_child

            # case 3
            # if both left & right, replace target with min node in right subtree, then delete
            else:
                # find min in right
                temp = node.right
                while temp.left:
                    temp = temp.left
                # swap data    
                node.data = temp.val
                # remove the node we swapped with
                node.right = self._remove(node.right, temp.data)
            
        elif elem < node.val:
            node.left = self._delete(node.left, elem)
        elif elem > node.val:
            node.right = self._delete(node.right, elem)
        else:
            return

        return node

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
            if elem < root.val:
                self._search(root.left, elem)
            else:
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
    binary_search_tree = BinarySearchTree()
    binary_search_tree.root = Node(1)

    binary_search_tree.traverse( TreeTraversalOrder.LEVEL_ORDER )


if __name__ == '__main__':
    main()