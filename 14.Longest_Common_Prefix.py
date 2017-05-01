class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        ans_i = 0
        for i in range(len(strs[0])):
            for str_ in strs:
                if len(str_) <= i or str_[i] != strs[0][i]:
                   return strs[0][:ans_i]
            else:
                ans_i = i + 1
        return strs[0][:ans_i]
