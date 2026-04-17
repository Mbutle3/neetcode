from collections import defaultdict
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        left = 0 
        right = 1
        sub_arr_count = 0 
        seen = defaultdict(list)
        n = len(arr) - 1

        while right < n:
            curr_count = 0
            curr_sum = 0
            while arr[right] not in seen:
                seen[arr[right]].append(arr[right])
            
            for v in seen[arr[right]].values():
                curr_count += 1
                curr_sum += v
            if curr_sum / curr_count > threshold and curr_count < k:
                sub_arr_count += 1 
        return sub_arr_count
            
            

        
        
        
        