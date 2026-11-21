# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        node = head
        while node:
            nex = node.next
            if nex in seen:
                return True
            node = nex
            if not node:
                return False
            seen.add(nex)
        return False 
        