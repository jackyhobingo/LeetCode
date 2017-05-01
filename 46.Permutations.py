class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def get_per_mute(start, end):
            if start == end:
                ans.append(nums[:])
            else:
                for i in range(start, end+1):
                    nums[start], nums[i] = nums[i], nums[start]
                    get_per_mute(start + 1, end)
                    nums[start], nums[i] = nums[i], nums[start]
        get_per_mute(0, len(nums)-1)
        
        return ans
