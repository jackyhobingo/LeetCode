class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    result += j == 0
                    result += j == len(grid[0]) - 1
                    result += i == 0
                    result += i == len(grid) - 1
                result += j < len(grid[0]) - 1 and grid[i][j] != grid[i][j+1]
                result += i < len(grid) - 1 and grid[i][j] != grid[i+1][j]
        return result
