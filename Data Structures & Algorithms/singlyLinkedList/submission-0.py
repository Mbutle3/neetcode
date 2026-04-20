class LinkedList:
    
    def __init__(self):
        self.head = []
        self.next = None
        length = 0

    def get(self, index: int) -> int:
        if self.length > index or index < 0:
            return -1
        ith = 0
        curr = self.head
        while curr:
            if ith == index:
                return curr
            else:
                curr = curr.next
                ith += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head = newNode
        

    def insertTail(self, val: int) -> None:
        curr = self.head
        while curr:
            curr = curr.next
        newNode = Node(val)
        curr.next = newNode
        newNode.next = None


    def remove(self, index: int) -> bool:
        if self.length > index or index < 0:
            return False
        ith = 0
        curr = self.head
        while curr:
            if ith == index - 1:
                curr.next = curr.next.next
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
        
