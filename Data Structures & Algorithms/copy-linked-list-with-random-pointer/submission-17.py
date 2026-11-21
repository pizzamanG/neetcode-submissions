class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        nodeDict = {}
        curr = head
        
        # Step 1: Create all copies
        while curr:
            nodeDict[curr] = Node(curr.val)   # ← FIXED: curr, not head!
            curr = curr.next
        
        # Step 2: Connect next and random
        curr = head
        while curr:
            copy = nodeDict[curr]
            copy.next = nodeDict.get(curr.next)
            copy.random = nodeDict.get(curr.random)
            curr = curr.next
        
        return nodeDict[head]



            
            





     