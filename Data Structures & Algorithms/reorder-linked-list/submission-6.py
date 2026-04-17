# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        length = 0

        curr = head

        #iterating to get the length
        while curr:
            length += 1
            curr = curr.next
        

        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
        
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            curr1,curr2 = curr2, curr1
            curr1 = curr1.next
            curr2 = curr2.next
        return curr1

        

        