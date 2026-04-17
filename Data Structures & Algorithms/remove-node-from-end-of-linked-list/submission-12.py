# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total_nodes = 0
        curr = head
        while curr:
            curr = curr.next
            total_nodes += 1

        idx = 0
        curr = head
        while curr and idx != total_nodes - n:
            curr = curr.next
            if curr and idx == total_nodes-n:
                curr.next = curr.next.next
        return curr


        
        