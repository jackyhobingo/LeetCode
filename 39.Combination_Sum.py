class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(now_list, sum_, n):
            for i in range(n, len(candidates)):
                temp_sum = sum_ + candidates[i]
                if temp_sum < target:
                    dfs(now_list + [candidates[i]], temp_sum, i)
                    continue
                if temp_sum == target:
                    ans.append(now_list + [candidates[i]])
                return 
        candidates.sort()
        dfs([], 0, 0)
        return ans
