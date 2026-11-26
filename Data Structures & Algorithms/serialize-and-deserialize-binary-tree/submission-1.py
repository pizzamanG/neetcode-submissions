# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        array = []

        def dfs(node):
            nonlocal array
            if node is None:
                array.append('#')
                return 

            array.append(str(node.val))

            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(array)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:


        arr = iter(data.split(','))
        def dfs():
            nonlocal arr
            val = next(arr)

            if val == '#':
                return None
            
           
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()

            return node
    

        return dfs()









