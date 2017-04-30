class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # """
        # :type nums1: List[int]
        # :type nums2: List[int]
        # :rtype: float
        # """
        a, b = sorted([nums1, nums2], key=len)
        m, n = len(a), len(b)
        
        half_len = (m + n + 1 ) // 2
        i_min = 0
        i_max = m
        
        while i_min <= i_max:
        
            i = (i_min + i_max) // 2
            j = half_len - i
        
            if i < m and b[j-1] > a[i]:
                i_min = i + 1
            elif i > 0 and a[i-1] > b[j]:
                i_max = i - 1
            else:
                if i == 0: 
                    max_of_left = b[j-1]
                elif j == 0: 
                    max_of_left = a[i-1]
                else: 
                    max_of_left = max(a[i-1], b[j-1])
        
                if (m + n) % 2 == 1:
                    return max_of_left
        
                if i == m: 
                    min_of_right = b[j]
                elif j == n: 
                    min_of_right = a[i]
                else: 
                    min_of_right = min(a[i], b[j])
        
                return (max_of_left + min_of_right) / 2.0