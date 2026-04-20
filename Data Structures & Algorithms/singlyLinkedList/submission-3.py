from typing import List

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length or index < 0:
            return -1
        ith = 0
        curr = self.head
        while curr:
            if ith == index:
                return curr.val
            else:
                curr = curr.next
                ith += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newHead.next = self.head
        self.head = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        if not self.head:  # Empty list
            self.insertHead(val)
            return    
        curr = self.head
        while curr.next:  # Stop at last node
            curr = curr.next
            
        curr.next = Node(val)
        self.length += 1


    def remove(self, index: int) -> bool:
        if index >= self.length or index < 0:
            return False
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return True
        ith = 0
        curr = self.head
        while curr:
            if ith == index - 1:
                curr.next = curr.next.next
                self.length -= 1
                return True
            else:
                curr = curr.next
                ith += 1
        return False

        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res
        
