class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.arr[i] if True else -1


    def set(self, i: int, n: int) -> None:
        if len(self.arr) > i:
            self.arr[i] = n
        


    def pushback(self, n: int) -> None:
        self.arr.append(n)


    def popback(self) -> int:
        return self.arr.pop(-1)

    def resize(self) -> None:
        len(self.arr) * 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return len(self.arr)
