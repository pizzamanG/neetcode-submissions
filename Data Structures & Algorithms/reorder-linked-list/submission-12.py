# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        count = 0
        tail= head
        while tail.next is not None:
            count +=1
            tail = tail.next
 
        midpoint = (count // 2)
       
        
        temp = head
        
        mid_count = 0 
        while mid_count < midpoint:
            temp = temp.next
            mid_count +=1



        second_half_head = temp.next
        temp.next = None
        
        prev = None
        curr = second_half_head

        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        second_half_head = prev

        dummy = ListNode()
        h = dummy


            
        while head is not None:
            temp = head.next

            dummy.next = head
            dummy = dummy.next

            if second_half_head is not None:
                dummy.next = second_half_head
                second_half_head = second_half_head.next
                dummy = dummy.next

            head = temp

        dummy.next = None
    
        
           

           





  
        

       


      
        

