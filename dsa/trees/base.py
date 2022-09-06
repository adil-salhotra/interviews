class TreeNode:
    def __init__(self, val=None, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root: TreeNode) -> None:
        self.root = root
    def __repr__(self) -> str:
        def level_order(root):
            if not root:
                return list()
            
            q = [root]
            level = 0
            levels = list()
            
            while q:
                
                levels.append(list())
                level_len = len(q)
                
                for _ in range(level_len):
                    node = q.pop(0)
                    if node:
                        levels[level].append(node.val)
                        if node.left:
                            q.append(node.left)
                        if node.right:
                            q.append(node.right)
                level += 1
            return levels

            
        return str(level_order(self.root))

    @classmethod
    def create_from_iter(cls, iter):
        if not iter:
            return Tree(TreeNode())

        def recursively_create(iter):
            if not iter:
                return

            num = iter.pop(0)
            new_node = TreeNode(num)
            new_node.left = recursively_create(iter)
            new_node.right = recursively_create(iter)
            return new_node

        if isinstance(iter, list):
            root = recursively_create(iter)
            return cls(root)
    


tree = Tree.create_from_iter([3,9,20,None,None,15,7])
print(tree)


            
                