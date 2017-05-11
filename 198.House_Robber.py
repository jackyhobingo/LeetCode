class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        contain_max = not_contain_max = 0
        for num in nums:
            contain_max, not_contain_max = max(not_contain_max + num, contain_max), contain_max
        return contain_max
