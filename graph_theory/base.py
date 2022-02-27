from typing import Iterable


class Graph:
    def __init__(self, representation: str, edges: Iterable, nodes: Iterable):
        """ 
            In an adjacency list, we have a graph represented
            as a list of unordered lists each of the unordered lists
            represents an edge between the two nodes in the list. 


        """
        self._representation = representation
        self._set_graph(edges, nodes)
        self._size = self._get_size()
        self._visited = [False] * self.size 

    @property
    def representation(self):
        return self._representation
    
    @property
    def visited(self):
        return self._visited
    
    @property
    def items(self):
        return self._items
    
    def _get_size(self):
        pass

    def _set_graph(self, edges, nodes):
        if self._representation == 'adjacency list':
            self._items = dict()
            for edge in edges:
                self._items

        if self._representation == 'adjacency matrix':
            self._items = list()

    def dfs(self, current):
        if self.visited[current]:
            return
        self.visited[current] = True
        neighbors = self.graph[current]
        for node in neighbors:
            self.dfs(node)
    
    def count_connected_components(self, current):
        pass


    


            
            

