"""
Graph implementation
    class GraphMatrix - adjacency matrix
"""
from enum import Enum, auto

class TraversalType(Enum):
    LEVEL_ORDER = auto()
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()
class GraphMatrix:
    """
    Graph implementation using an adjacency matrix
    [
     [ ]
     [ ]
     [ ]
    ]
    """

    def __init__(self, graph_matrix: list = None):
        """ Inits Graph class with optional graph_matrix """
        self.graph_matrix = graph_matrix

def main():
    pass