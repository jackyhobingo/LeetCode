class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.split(" ")
        l = [i[::-1] for i in l]
        return ' '.join(l)
