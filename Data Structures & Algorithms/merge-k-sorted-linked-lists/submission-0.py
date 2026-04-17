# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        curr = lists

        dummy.next = curr
        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return dummy.next