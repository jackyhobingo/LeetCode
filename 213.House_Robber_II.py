class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_contain = [0, 0]
        max_not_contain = [0, 0]
        for num in nums[1:]:
            max_contain[0], max_not_contain[0] = max(max_contain[0], max_not_contain[0] + num), max_contain[0]
        for num in nums[:-1]:
            max_contain[1], max_not_contain[1] = max(max_contain[1], max_not_contain[1] + num), max_contain[1]
        return max(max_contain) if len(nums) > 1 else max(nums or [0])
