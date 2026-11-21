# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(node):

            if not node:
                return None
                
            else:
                temp = node.left
                node.left = node.right
                node.right = temp
                rev(node.left)
                rev(node.right)
        
        rev(root)
        return root
            
            
               

        