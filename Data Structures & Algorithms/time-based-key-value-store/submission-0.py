class TimeMap:

    def __init__(self):
        self.tMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tMap:
            self.tMap[key] = []
        self.tMap[key].append((value, timestamp))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tMap:
            return ""
        arr = self.tMap[key]  # list of (timestamp, value)
        # Binary search for rightmost timestamp <= given timestamp
        i = bisect.bisect_right(arr, (timestamp, chr(127)))  # max char to ensure correct comparison
        if i == 0:
            return ""
        return arr[i - 1][1]
        
