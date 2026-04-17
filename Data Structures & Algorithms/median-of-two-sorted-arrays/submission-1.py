class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1) - 1
        m = len(nums2) - 1
        isOdd = False
        
        if (n + m) % 2 == 1:
            isOdd = True

        n_median_value = nums1[n // 2]
        m_median_value = nums2[m // 2]

        

        return (n_median_value + m_median_value) if isOdd else (n_median_value + m_median_value) / (n + m)
        