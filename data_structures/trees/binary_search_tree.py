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