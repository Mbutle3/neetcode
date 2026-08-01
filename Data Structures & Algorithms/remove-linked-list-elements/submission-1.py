# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        if curr.val == val:
            tmp = curr.next
            curr = None
            head = tmp
            return
            
        
        while curr:
            if curr.next.val == val:
                curr = curr.next.next
            curr = curr.next
        
        return head
                