class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """ 
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            space = [n for num in nums for n in num]
            return [space[c*i:c*i+c] for i in range(r)]
