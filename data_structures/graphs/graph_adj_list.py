"""
Graph implementation
    class Graph - adjacency list
"""

class Graph:
    """
    Graph implementation using an adjacency list
        { '1' : {x,x,x,} #set
          '2' : {x,x,x,} #set
          '3' : {x,x,x,} #set
        }
    """

    def __init__(self, graph_dict: dict = {}):
        """ Inits Graph class with optional graph_dict """
        self.graph_dict = graph_dict

    def edges(self, vertice: int):
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

    def add_vertex(self, vertex: int):
        """ adds a new vertex to the graph if it doesn't exist """
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = set()

    def add_edge(self, edge: list):
        """ add an edge between two vertices """
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self.graph_dict:
                self.graph_dict[x].add(y)
            else:
                self.graph_dict[x] = {y}

    def _generate_edges(self):
        """ generates the edges of a graph """
        edges = []
        for vertex in self.graph_dict:
            for neighbour in self.graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def has_edge(self, vertices: list):
        """ checks if there's an edge between two given vertices """
        if len(vertices) == 2:
            v1, v2 = vertices
            if self.has_vertex(v1) and self.has_vertex(v2):
                if v2 in self.graph_dict[v1] and v1 in self.graph_dict[v2]:
                    return True

        return False

    def has_vertex(self, vertex: int):
        """ checks if the given vertex exists """
        if vertex in self.graph_dict:
            return True
        return False

    def delete_edge(self, vertices: list):
        """ removes the edge between two given vertices - if it exists """
        if self.has_edge(vertices):
            v1, v2 = vertices
            self.graph_dict[v1].remove(v2)
            self.graph_dict[v2].remove(v1)
            return True

        return False

    def delete_vertex(self, vertex: int):
        """ removes the given vertex and therefore the edges to it """
        if self.has_vertex(vertex):
            del self.graph_dict[vertex]
            for neighbours in self.graph_dict.values():
                if vertex in neighbours:
                    neighbours.remove(vertex)
            return True
        return False

    def level_order_traversal(self):
        """ traverses graph level-order -  """
        pass

    def dfs_traversal(self, node):
        """ traverses graph in a dfs style - O(V+E) """
        visited = set()
        self._dfs(visited, node)

    def _dfs(self, visited, node):
        """ helper method to recursively DFS graph """
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in self.graph_dict[node]:
                self._dfs(visited,neighbour)


if __name__ == '__main__':
    # 0 -- 1
    # |
    # | 
    # 2 -- 3 -- 4
    # |  /
    # | /
    # 5
    g = Graph()
    g.add_vertex(0)
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(4)
    g.add_vertex(5)

    # add
    print('Adding edges...')
    g.add_edge([0,1])
    g.add_edge([0,2])
    g.add_edge([2,3])
    g.add_edge([2,5])
    g.add_edge([3,4])
    g.add_edge([3,5])

    # traversal
    print('*** DFS ***')
    g.dfs_traversal(0)

    # show
    print('***Has edge?***')
    print( g.has_edge([0,1]) )
    print('***Edges of 0:***')
    print( g.edges(0) )
    print('***Edges of 1:***')
    print( g.edges(1) )
    print('***Edges of 2:***')
    print( g.edges(2) )
    print('***All edges:***')
    print( g.all_edges() )
    print('***All vertices:***')
    print( g.all_vertices() )

    print('***All vertices:***')
    print( g.all_vertices() )

    # delete
    print('***Delete vertex 1:***')
    print( g.delete_vertex(1) )
    print('***Has vertex 1?:***')
    print( g.has_vertex(1) )
    print('***Has edge 0,1?:***')
    print( g.has_edge([0,1]) )
    print('***Delete edge 3,5:***')
    print( g.delete_edge([3,5]) )
    print('***Has edge 3,5?:***')
    print( g.has_edge([3,5]) )

    # traversal
    print('*** DFS ***')
    g.dfs_traversal(0)