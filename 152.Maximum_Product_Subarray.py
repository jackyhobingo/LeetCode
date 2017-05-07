class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums):
        max_here = min_here = max_ = nums[0]

        for i in range(1, len(nums)):
            min_here, temp, max_here = sorted([max_here * nums[i] , min_here * nums[i], nums[i]])
            max_ = max(max_here, max_)
        return max_
