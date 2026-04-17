# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head.next
        fast = head.next.next

        while head:
            temp = slow
            slow = fast.next
            fast = fast.next.next
        return head
        

        