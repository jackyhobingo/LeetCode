class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s

        max_length = 1
        x, y = 0, 1
        
        for i in range(1, len(s)):
            if i + max_length // 2 >= len(s):
                break
            for j in range(max_length // 2, len(s)//2 + 1):
                has_palindrome = False
                if i - j >= 0 and i + j + 1 <= len(s):
                    temps1 = s[i-j:i+j+1] 
                    if temps1 == temps1[::-1]:
                        has_palindrome = True
                        if max_length < len(temps1):
                            x, y = i-j, i+j+1
                            max_length = len(temps1)
                
                if i - j - 1 >= 0 and i + j + 1 <= len(s):    
                    temps2 = s[i-1-j:i+j+1]
                    if temps2 == temps2[::-1]:
                        has_palindrome = True
                        if max_length < len(temps2):
                            x, y = i-j-1, i+j+1
                            max_length = len(temps2)
                if not has_palindrome:
                    break
                
        return s[x:y]
