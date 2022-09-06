class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    
    def instantiate(cls, data):
        try:
            return cls._instantiate_list(data)
        except:
            NotImplementedError("Need a list format to deserialize binary tree.")
    
    def _instantiate_list(cls, data):
        if not isinstance(data, list):
            return -1
        while data:
            curr_val = data[0]
            data.pop()
            if curr_val == 'None':
                return
            
            new_node = TreeNode(curr_val)
            new_node.left = cls._instantiate_list(data)
            new_node.right = cls._instantiate_list(data)

            return new_node
    
    

            


