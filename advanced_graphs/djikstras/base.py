class Graph:
    def __init__(self):
        self.vertices = dict()

    def add_vertex(self, node, edges):
        self.vertices[node] = edges

    def shortest_path(self, start_node, end_node):
        
        
