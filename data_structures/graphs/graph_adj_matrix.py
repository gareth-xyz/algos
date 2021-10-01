"""
Graph implementation
    class GraphMatrix - adjacency matrix
"""
from collections import deque

class GraphMatrix:
    """
    Graph implementation using an adjacency matrix
    [
     [ ]
     [ ]
     [ ]
    ]
    """

    def __init__(self, size: int):
        """ Inits Graph class with optional graph_matrix """
        self.graph_matrix = []
        for _ in range(size):
            self.graph_matrix.append([0 for _ in range(size)])
        self.size = size

    def add_edge(self, edge: list):
        """ add an edge between two vertices """
        if not self.has_edge(edge):
            v1, v2 = edge
            self.graph_matrix[v1][v2]
            self.graph_matrix[v2][v1]
            return True
        return False

    def delete_edge(self, edge: list):
        """ removes the edge between two given vertices - if it exists """
        if self.has_edge(edge):
            v1, v2 = edge
            self.graph_matrix[v1][v2] = 0
            self.graph_matrix[v2][v1] = 0
            return True
        return False

    def has_edge(self, vertices: list):
        """ checks if there's an edge between two given vertices """
        if len(vertices) == 2:
            v1, v2 = vertices
            if self.graph_matrix[v1][v2] and self.graph_matrix[v2][v1]:
                return True
        return False

    def bfs_traversal(self, node):
        """ traverses graph level-order -  """
        self._bfs(node)

    # def _bfs(self, node):
    #     """ helper method to BFS graph """
    #     visited = [node]
    #     queue = deque()
    #     queue.append(node)

    #     while queue:
    #         node = queue.popleft()
    #         print(node)
            
    #         for neighbour in self.graph_matrix[node]:
    #             if neighbour not in visited:
    #                 queue.append(neighbour)
    #                 visited.append(neighbour)

    # def dfs_traversal(self, node):
    #     """ traverses graph in a dfs style - O(V+E) """
    #     visited = set()
    #     self._dfs(visited, node)

    # def _dfs(self, visited, node):
    #     """ helper method to recursively DFS graph """
    #     if node not in visited:
    #         print(node)
    #         visited.add(node)
    #         for neighbour in self.graph_dict[node]:
    #             self._dfs(visited,neighbour)


if __name__ == '__main__':
    # 0 -- 1
    # |
    # | 
    # 2 -- 3 -- 4
    # |  /
    # | /
    # 5
    g = GraphMatrix(5)

    # add
    print('Adding edges...')
    g.add_edge([0,1])
    g.add_edge([0,2])
    g.add_edge([2,3])
    g.add_edge([2,5])
    g.add_edge([3,4])
    g.add_edge([3,5])
    g.add_edge([5,6])
    g.add_edge([6,7])
    g.add_edge([7,8])

    # show
    print('***Has edge?***')
    print( g.has_edge([5,3]) )
    
    # delete edge
    print('***Delete edge: 5,3:***')
    print( g.delete_edge([5,3]) )

    # show
    print('***Has edge?***')
    print( g.has_edge([5,3]) )

    # traversal
    print('*** DFS ***')
    g.dfs_traversal(0)
    
    print('*** BFS ***')
    g.dfs_traversal(0)
    