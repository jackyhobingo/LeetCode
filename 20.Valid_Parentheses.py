class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2: return False
        
        p_dict = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif len(stack) != 0:
                pre_one = stack.pop()
                if p_dict[pre_one] != c:
                    return False
            else:
                return False
        return False if len(stack) else True
