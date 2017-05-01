class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: 
            return s
        new_list = [[] for i in range(numRows)]

        inc = True
        j = 0
        for i in range(len(s)):
            new_list[j].append(s[i])
            if inc:
                j += 1
                if j == numRows:
                    j = numRows - 2
                    inc = False
            else:
                j -= 1
                if j == -1:
                    j = 1
                    inc = True
        
        return ''.join([''.join(list_) for list_ in new_list])
