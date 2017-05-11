class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ans = []
        def back_tracking(pre_list, pre_sum, pre_i, times):
            if times == 0:
                return 
            for i in range(pre_i + 1, 10):
                new_sum = pre_sum + i
                if new_sum < n:
                    back_tracking(pre_list + [i], new_sum, i, times - 1)
                    continue
                elif new_sum == n and times == 1:
                    ans.append(pre_list + [i])
                return
        back_tracking([], 0, 0, k)
        return ans
