class Solution(object):
    
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_list = sorted(nums)
        result = 0
        i = 0
        for _ in sorted_list:
            i += 1
            if i % 2:
                result += _ 
            
        return result