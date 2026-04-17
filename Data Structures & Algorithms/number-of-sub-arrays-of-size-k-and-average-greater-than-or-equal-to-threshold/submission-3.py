class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #Get the total length of the arr
        n = len(arr)

        #if the arr is shorter than k, there cant be any valid subarrays
        if n < k:
            return False
        
        #Pre Calculate what the total sum of a valid window must reach
        target = k * threshold

        #Calculate the sum of the first window
        window_sum = sum(arr[:k])

        #Initalize count to 1 if the first window meets of exceeds the thresehold otherwise set to 0
        count = 1 if window_sum >= threshold else 0

        #SLide the window one step at a time from k until n
        for i in range (k, n):
            #add the next lement and remove the element that falls out 
            #next element = arr[i] element that falls out arr[i - k]
            window_sum += arr[i] - arr[i - k]

            #if this new window sum meets or exceeds the threshold, increment the count
            if window_sum >= target:
                count += 1
        return count
            

