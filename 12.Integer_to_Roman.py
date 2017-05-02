class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def get_roman(digit, ten, five, one):
    
            if digit == 9:
                return one + ten
            elif digit == 4:
                return one + five
            elif digit > 3:
                return five + one * (digit % 5)
            else:
                return one * digit
        
        n = [num // 1000 % 10, num // 100 % 10, num // 10 % 10, num % 10]
        
        return get_roman(n[0], "", "", "M") + get_roman(n[1], "M", "D", "C") + get_roman(n[2], "C", "L", "X") + get_roman(n[3], "X", "V", "I")
