# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head 

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow

        l2 = mid.next
        mid.next = None 

        prev = None
        while l2:
            nxt = l2.next
            l2.next = prev 
            prev = l2
            l2 = nxt 

        l2_head = prev

        while l2_head:
            n1 = head.next
            n2 = l2_head.next

            head.next = l2_head
            l2_head.next = n1

            head = n1
            l2_head = n2
   


        

   

     

            
