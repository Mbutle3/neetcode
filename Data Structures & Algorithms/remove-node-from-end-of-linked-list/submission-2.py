class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPtr = dummy.next
        rightPtr = head


        for _ in range(n):
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next
            leftPtr = leftPtr.next.next

        return dummy.next


    
        """
        Create a dummy node to safely handle cases where the head itself is removed

        Set left pointer to the dummy (one node before head)

        Set right pointer to the actual head

        Move the right pointer n steps ahead to create a gap of n nodes

        Move both pointers together until right reaches the end

        At this point, left is right before the node that must be removed

        Skip the target node by adjusting left's next pointer

        Return the new head (which is dummy.next)
         """    
