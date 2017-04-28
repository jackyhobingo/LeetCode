class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        
        if len_nums < 3:
            return 0
        
        nums.sort()
        result = sum(nums[:3])
        
        for i in range(len_nums - 2):

            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len_nums - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]
                result = s if abs(s-target) < abs(result-target) else result
                    
                if s - target < 0:
                    j += 1
                elif s - target > 0:
                    k -= 1
                else:
                    return s
        return result
