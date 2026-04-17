# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. Edge Cases
        if not head or not head.next:
            return
        #2. Find the middle
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #3. Reverse the second half
        second_half = slow.next
        prev = None
        slow.next = None

        while second_half:
            nxt = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = nxt
        
        #4. Merge Alternatively
        firstPtr = head
        secondPtr = prev

        while secondPtr:
            tmp1 = firstPtr.next
            tmp2 = secondPtr.next
            
            firstPtr.next = secondPtr
            secondPtr.next = tmp1 

            firstPtr = tmp1.next
            secondPtr = tmp2.next