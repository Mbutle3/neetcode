class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # strip all leading matches
        while head and head.val == val:
            head = head.next

        curr = head
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next  # unlink, don't advance curr
            else:
                curr = curr.next             # only advance when no removal happened

        return head