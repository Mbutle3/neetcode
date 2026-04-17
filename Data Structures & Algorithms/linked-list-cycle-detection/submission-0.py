# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head

        slow = curr.next
        fast = curr.next.next

        while slow and fast:
            if slow.val == fast.val:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
        