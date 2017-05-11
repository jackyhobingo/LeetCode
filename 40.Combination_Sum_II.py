class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        def dfs(l, sum_, start_n):
            last_temp_sum = sum_
            for i in range(start_n, len(candidates)):
                temp_sum = sum_ + candidates[i]
                new_l = l + [candidates[i]]
                if temp_sum < target:
                    if last_temp_sum == temp_sum:
                        continue
                    last_temp_sum = temp_sum
                    dfs(new_l, temp_sum, i + 1)
                    continue
                if temp_sum == target:
                    ans.append(new_l)
                return 
        dfs([], 0, 0)
        return ans
