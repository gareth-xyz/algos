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
            self.graph_matrix[v1][v2] = 1
            self.graph_matrix[v2][v1] = 1
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
        """ traverses graph level-order -  O(v^2) """
        self._bfs(node)

    def _bfs(self, node):
        """ helper method to BFS graph """
        visited = [node]
        queue = deque()
        queue.append(node)

        while queue:
            node = queue.popleft()
            print(node)

            for i in range(len(self.graph_matrix)):
                temp = self.graph_matrix[node][i]
                if temp != 0 and i not in visited:
                    queue.append(i)
                    visited.append(i)

    def dfs_traversal(self, node):
        """ traverses graph in a dfs style - O(v^2) """
        visited = set()
        self._dfs(visited, node)

    def _dfs(self, visited, node):
        """ helper method to recursively DFS graph """
        if node not in visited:
            print(node)
            visited.add(node)

            for i in range(len(self.graph_matrix[node])):
                if self.graph_matrix[node][i] != 0:
                    self._dfs(visited,i)


if __name__ == '__main__':
    # 0 -- 1
    # |
    # | 
    # 2 -- 3 -- 4
    # |  /
    # | /
    # 5
    g = GraphMatrix(6)

    # add
    print('Adding edges...')
    g.add_edge([0,1])
    g.add_edge([0,2])
    g.add_edge([2,3])
    g.add_edge([2,5])
    g.add_edge([3,4])
    g.add_edge([3,5])
    # show
    print('***Has edge?***')
    print( g.has_edge([5,3]) )
    
    #delete edge
    print('***Delete edge: 5,3:***')
    print( g.delete_edge([5,3]) )

    # # show
    print('***Has edge?***')
    print( g.has_edge([5,3]) )

    # # traversal
    print('*** DFS ***')
    g.dfs_traversal(0)
    
    print('*** BFS ***')
    g.bfs_traversal(0)
    