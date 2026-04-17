# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, curr2 = list1, list2
        return_list = ListNode(0)
        dummy = return_list.next

        while curr1 and curr2:
            if curr1.val < curr2.val:
                dummy = curr1
                curr1 = curr1.next
            else:
                dummy = curr2
                curr2 = curr2.next
            dummy = dummy.next
        
        while curr1:
            dummy = curr1
            curr1 = curr1.next

        while curr2:
            dummy = curr2
            curr2 = curr2.next
        
        return dummy.next
            
