class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_digits(self, n):
            digits = []
            while n:
                digits.append(n % 10)
                n /= 10
            return digits
        
        digits_l = []
        while n:
            digits = get_digits(n)
            if digits in digits_l:
                return False
            digits_l.append(digits)
            n = sum([digit**2 for digit in digits])
            if n == 1:
                return True
