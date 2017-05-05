class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1]
        
        for i in range(1, len(nums)):
            ans.append(ans[i-1] * nums[i-1])
        right = 1
        for i in range(len(nums) - 2, -1, -1):
            right *= nums[i + 1]
            ans[i] *= right
        
        return ans
