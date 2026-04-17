"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None}
        curr = head
        #First Pass - Clone Linked List Nodes and Add To Seen
        while curr:
            copy = Node(curr.val)
            seen[curr] = copy
            curr = curr.next
        #Second Pass - Set Pointers
        curr = head
        while curr:
            copy = seen[curr]
            curr.next = seen[curr.next]
            curr.random = seen[curr.random]
            curr = curr.next
        return seen[head]
            
        