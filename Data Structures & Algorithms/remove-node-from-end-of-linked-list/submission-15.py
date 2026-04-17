class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Move right n steps ahead
        while n > 0:
            right = right.next
            n -= 1

        # Move both pointers
        while right:
            left = left.next
            right = right.next

        # Delete node
        left.next = left.next.next

        return dummy.next