# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find The Middle
        # Example: [0, 1, 2, 3, 4, 5, 6]
        # slow moves 1 step, fast moves 2 steps:
        #   slow = 0, fast = 0
        #   slow = 1, fast = 2
        #   slow = 2, fast = 4
        #   slow = 3, fast = 6
        # fast reached the end, so middle = 3

        # Reverse Second Half
        # Original: [0, 1, 2, 3, | 4, 5, 6]
        # Cut after middle: first half = [0,1,2,3], second half = [4,5,6]
        # Reverse the second half:
        #   [4,5,6] -> [6,5,4]
        # Combined conceptual view:
        #   [0, 1, 2, 3, 6, 5, 4]

        # Merge first half and reversed second half alternately
        # first:  [0, 1, 2, 3]
        # second: [6, 5, 4]
        #
        # Step-by-step weaving:
        #   0 -> 6 -> 1 -> 5 -> 2 -> 4 -> 3
        #
        # Final reordered list:
        #   [0, 6, 1, 5, 2, 4, 3]


        #Step 1: Find The Middle 
        fast = head
        slow = head
        middle = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #Step 2: Reverse The Second Half
        second = slow.next
        slow.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        
        # Step 3: Merge first half (head) and reversed second half (prev)
        first = head
        second = prev

        while second:
            tmp1 = first.val
            tmp2 = second.val

            first.next = second
            second.next = tmp1

            first = tmp1 
            second = tmp2


        


