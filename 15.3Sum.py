class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        end = len(sorted_nums)
        ans_list = []
        for i in range(end - 2):
            if i != 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            k = end - 1
            j = i + 1
            while j < k:
                s = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if s < 0:
                    j += 1
                elif s > 0 :
                    k -= 1
                else:
                    ans_list.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    while j < k and sorted_nums[j] == sorted_nums[j+1]:
                        j += 1
                    while j < k and sorted_nums[k] == sorted_nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
        return ans_list
