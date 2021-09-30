"""
Graph implementations
    class Graph - adjacency list
    class GraphMatrix - adjacency matrix
"""
from enum import auto

class TraversalType(Enum):
    LEVEL_ORDER = auto()
    PRE_ORDER = auto()
    IN_ORDER = auto()
    POST_ORDER = auto()

class Graph:
    """
    Graph implementation using an adjacency list

        { '1' : {x,x,x,} #set
          '2' : {x,x,x,} #set
          '3' : {x,x,x,} #set
        }

    """

    def __init__(self, graph_dict: dict = None):
        """ Inits Graph class with optional graph_dict """
        self.graph_dict = graph_dict

    def edges(self, vertice):
        """ Retrieves the edges of the given vertice if it exists in the graph """
        if vertice in self.graph_dict:
            return self.graph_dict[vertice]
        else:
            return False

    def all_vertices(self):
        """ retrieves the vertices of a graph as a set """
        return set(self.graph_dict.keys())

    def all_edges(self):
        """ returns the edges of the graph """
        return self._generate_edges()

    def add_vertex(self, vertex):
        """ adds a new vertex to the graph if it doesn't exist """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        """ add an edge between two vertices """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self.graph_dict:
                self.graph_dict[x].add(y)
            else:
                self.graph_dict[x] = y

    def _generate_edges(self):
        """ generates the edges of a graph """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighber, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def has_edge(self, vertices):
        """ checks if there's an edge between two given vertices """
        if len(vertices) == 2:
            v1, v2 = vertices
            if self.has_vertex(v1) and self.has_vertex(v2):
                if v2 in self.graph_dict[v1] and v1 in self.graph_dict[v2]:
                    return True

        return False

    def has_vertex(self, vertex):
        """ checks if the given vertex exists """
        if vertex in self.graph_dict:
            return True
        return False

    def delete_edge(self, vertices):
        """ removes the edge between two given vertices - if it exists """
        if self.has_edge(vertices):
            v1, v2 = vertices
            self.graph_dict[v1].remove(v2)
            self.graph_dict[v2].remove(v1)
            return true

        return False

    def delete_vertex(self, vertex):
        """ removes the given vertex and therefore the edges to it """
        if self.has_vertex(vertex):
            del self.graph_dict[vertex]
            for neighbours in self.graph_dict.values():
                if vertex in neighbours:
                    neighbours.remove(vertex)
            return True
        return False

    def traverse(self, traverse_type):
        """ traverses the graph using the given traverse type """
        if traverse_type == TraversalType.LEVEL_ORDER:
            return self._level_order_traversal(self.graph_dict)
        if traverse_type == TraversalType.PRE_ORDER:
            return self._pre_order_traversal(self.graph_dict)
        if traverse_type == TraversalType.IN_ORDER:
            return self._in_order_traversal(self.graph_dict)
        if traverse_type == TraversalType.POST_ORDER:
            return self._post_order_traversal(self.graph_dict)

    def _level_order_traversal(self, node):
        """ """
        pass

    def _pre_order_traversal(self, node):
        """ """
        pass

    def _in_order_traversal(self, node):
        """ """
        pass

    def _post_order_traversal(self, node):
        """ """
        pass

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
