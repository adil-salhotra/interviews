"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node:
    def __init__(self, val, neighbors=list())
        self.val = val
        self.neighbors = neighbors
"""
from base import Node

def clone_graph(node: Node) -> Node:
    visited = dict() 

    def dfs(node):   
        if not node:
            return 
        if node in visited:
            return visited[node]
        
        copy = Node(node.val)
        visited[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))
        
        return copy
    
    if not node: return
    return dfs(node)
