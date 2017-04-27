class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(visited_list, m, M, len_M):
            visited_list[m] = True
            for n in range(len_M):
                if not visited_list[n] and M[m][n]:
                    dfs(visited_list, n, M, len_M)
        
        visited_list = [False for i in range(len(M))]
        ans = 0
        for m in range(len(M)):
            if not visited_list[m]:
                dfs(visited_list, m, M, len(M))
                ans += 1
    
        return ans
 