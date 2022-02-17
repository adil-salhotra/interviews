class Graph:
    def __init__(self, graph, size):
        """ In an adjacency list, we have a graph represented
            as a list of unordered lists each of the unordered lists
            represents an edge between the two nodes in the list. 
        """
        self.graph = graph
        self.size = size
        self.visited = [False] * self.size 

    def dfs(self, current):
        if self.visited[current]:
            return
        self.visited[current] = True
        neighbors = self.graph[current]
        for node in neighbors:
            self.dfs(node)
    
    def count_connected_components(self, current):
        pass


    


            
            

