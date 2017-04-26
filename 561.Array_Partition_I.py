class Solution(object):
    
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_list = sorted(nums)
        return sum(sorted_list[::2])
