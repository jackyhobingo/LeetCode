class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_all = reduce(operator.xor, nums)  # Do xor to all will become ans1 xor ans2.
        bit = xor_all & -xor_all  # Get a bit that is different between ans1 and ans2.
        ans = [0, 0]
        for n in nums:
            if bit & n:  
                ans[0] ^= n
            else:
                ans[1] ^= n
        return ans
