class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        for row in range(len(grid) - 1):
            grid[row+1][0] += grid[row][0]
        for col in range(len(grid[0]) - 1):
            grid[0][col+1] += grid[0][col]
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] += min(grid[row][col - 1], grid[row - 1][col])
        return grid[-1][-1]
