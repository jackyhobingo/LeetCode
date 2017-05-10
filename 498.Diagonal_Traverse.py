class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        result = []
        i_max, j_max = len(matrix), len(matrix[0])
        i = j = 0
        change_value = -1
        
        for s in range(i_max+j_max-1):
            (i, j) = (s, 0) if change_value < 0 else (0, s)
            if i >= i_max:
                i = i_max - 1
                j = s - i
            elif j >= j_max:
                j = j_max - 1
                i = s - j
            while i_max > i >= 0 and j_max > j >= 0:
                result.append(matrix[i][j])
                i += change_value
                j -= change_value
            change_value = -change_value
        
        return result
