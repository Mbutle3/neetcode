# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Stack:
    def __init__(self):
        
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.mini_stack[-1] if self.mini_stack else val)
        self.mini_stack.append(val)


class Solution: 

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        myStack = Stack()

        for val in lists:
            myStack.push(val)
        return myStack
        
