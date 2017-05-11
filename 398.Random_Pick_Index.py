class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        ans_list = []
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                ans_list.append(i)
        return random.sample(ans_list, 1)[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
