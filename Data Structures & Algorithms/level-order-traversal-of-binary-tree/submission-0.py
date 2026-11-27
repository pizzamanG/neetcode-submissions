# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = {}
        from collections import deque
        level = 0
        q = deque([(root, level)])

        
        while q:
            node, level = q.popleft()
            if node is not None:
                nodes.setdefault(level, []).append(node.val)
                level = level +1
                q.append((node.left, level))
                q.append((node.right, level))

        arr = []

        for _, val in nodes.items():
            arr.append(val)
        return arr






        