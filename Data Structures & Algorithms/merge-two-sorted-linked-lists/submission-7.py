# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        h = dummy

        while list1 is not None and list2 is not None:

            if list1.val < list2.val:
                dummy.next = list1
                temp = list1.next
                list1.next = None
                list1 = temp
                dummy = dummy.next
            
            elif list2.val <= list1.val:
                dummy.next = list2
                temp = list2.next
                list2.next = None
                list2 = temp
                dummy = dummy.next

        if list1 is not None:
            dummy.next = list1
        elif list2 is not None:
            dummy.next = list2
        
        return h.next
        