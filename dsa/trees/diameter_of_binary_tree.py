"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
from base import TreeNode

def diameter(root:TreeNode):
    ans = [0]

    def dfs(node):
        # If the subtree is a Null subtree (the node is None) then we say the height is -1
        if not node:
            return -1
        
        left = dfs(node.left)
        right = dfs(node.right)

        # we add 2 for 2 outgoing edges.
        ans[0] = max(ans[0], 2 + left + right)

        return 1 + max(left,right)
    
    dfs(root)
    return ans[0]
