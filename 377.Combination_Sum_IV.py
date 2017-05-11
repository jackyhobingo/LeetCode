class Solution(object):
    
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()

            
        ans = {0:1}
        for i in range(target + 1):
            for num in nums:
                if num > i:
                    break
                elif num == i:
                    ans[i] = ans.get(i, 0) + 1
                else:
                    ans[i] = ans.get(i, 0) + ans.get(i - num, 0)
        return ans.get(i, 0)
