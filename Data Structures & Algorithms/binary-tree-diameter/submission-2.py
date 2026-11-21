# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        def diameter(node):
            if not node:
                dia = 0
                return 0
            
            left = height(node.left)
            right = height(node.right)

            dia = max(diameter(node.left), diameter(node.right), left+right)
            return dia
        
        return diameter(root)
        

        
            
            

     
      
                


        