class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_ = 0
        roman_value = { 'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        reverse_s = s[::-1]
        
        for i in range(len(reverse_s)):
            if i != 0:
                new_v, pre_v = roman_value[reverse_s[i]], roman_value[reverse_s[i-1]]
                sum_ = sum_ + new_v if new_v >= pre_v else sum_ - new_v
            else:
                sum_ = roman_value[reverse_s[0]]
        
        return sum_
