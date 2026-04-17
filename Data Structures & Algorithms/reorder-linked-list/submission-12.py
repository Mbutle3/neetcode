# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #1. Empty Check
        if not head or not head.next:
            return
        
        #2. Find Middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #3. Reverse 2nd Half Of List
        curr = slow
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        #4. Merge Atlernately
        firstPtr = head
        secondPtr = prev

        while secondPtr:
            #store next 
            tmp1 = firstPtr.next
            tmp2 = secondPtr.next

            #link firstPtr to secondPtr
            firstPtr.next = secondPtr
            
            #link second to next of firstPtr
            secondPtr.next = tmp1

            firstPtr = tmp1
            secondPtr = tmp2 


        
        