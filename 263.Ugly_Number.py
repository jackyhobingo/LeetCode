class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        while num != 1 and num != 0:
            if not num % 2:
                num /= 2
            elif not num % 3:
                num /= 3
            elif not num % 5:
                num /= 5
            else:
                return False
        return True
