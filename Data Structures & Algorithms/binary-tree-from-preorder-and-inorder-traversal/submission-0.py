# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        

        pre = iter(preorder)
        dic = {num: i for i, num in enumerate(inorder)}

        def dfs(l,r):
            if l > r:
                return None

            node = TreeNode(next(pre))
            mid = dic[node.val]

            node.left = dfs(l, mid-1)
            node.right = dfs(mid+1, r)

            return node
        
        return dfs(0, len(preorder)-1)


        
            


            



