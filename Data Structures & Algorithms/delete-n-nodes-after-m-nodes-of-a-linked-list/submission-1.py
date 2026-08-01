# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head

        while curr:
            #same m nodes
            mCounter = m - 1
            while curr and mCounter > 0:
                curr = curr.next
                mCounter -= 1
            
            #delete next n nodes
            save_point = curr.next
            nCounter = n

            while save_point and nCounter > 0:
                save_point = save_point.next
                nCounter -= 1

            curr.next = save_point
            curr = save_point
        return head
        