class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        nodeDict = {}
        curr = head
        while curr:
            nodeDict[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        
        while curr:
            copy = nodeDict[curr]
            copy.next = nodeDict.get(curr.next)
            copy.random = nodeDict.get(curr.random)
            curr = curr.next
           
        
        return nodeDict[head]

        


        



    


            
            





     