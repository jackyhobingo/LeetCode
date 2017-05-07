class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        int_list = [ord(c) for c in list(s + t)]
        return chr(reduce(operator.xor, int_list))
