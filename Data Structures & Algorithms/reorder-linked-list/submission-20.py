# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. empty check
        if not head or not head.next:
            return
        #2. find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #3. reverse 2nd half
        second = slow
        prev = None
        slow.next = None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        #4. merge alternatively 
        firstPtr = head
        secondPtr = second
        while second:
            tmp1 = firstPtr.next
            tmp2 = secondPtr.next
            firstPtr.next = tmp2
            secondPtr.next = firstPtr
        
