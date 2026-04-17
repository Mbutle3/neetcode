# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        #1. create pointers Dummy-> ListNode(0, head); leftPtr = Dummy; rightPtr = head
        leftPtr = dummy
        rightPtr = head
        #2. move rightPtr up `n` positions
        for _ in range(n):
            rightPtr = rightPtr.next
        #3. move leftPtr and rightPtr together
        while rightPtr:
            leftPtr = leftPtr.next
            rightPtr = rightPtr.next
        #4. skip over the element we want to remove using leftPtr
        leftPtr.next = leftPtr.next.next
        #5. return linked list
        return dummy.next