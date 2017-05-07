class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        else:
            s = 0
            while num > 0:
                s += num % 10
                num /= 10
            return self.addDigits(s)
