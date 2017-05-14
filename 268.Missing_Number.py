import functools
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return functools.reduce(operator.xor, [i ^ nums[i] for i in range(len(nums))] + [len(nums)])
