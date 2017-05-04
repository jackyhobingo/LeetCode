class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for x in nums:
            if nums[abs(x) - 1] < 0: 
                result.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return result
