# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # 1. find mid
        # 2. reverse
        # 3. compare vals
        # 4. return T/F

        # 1 finding mid
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 2. reversing 1st half
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 3. compare

        h1 = slow
        h2 = prev
        while h1 and h2:
            if h1.val != h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        
        if not h1 and not h2:
            return True
        else:
            False

        