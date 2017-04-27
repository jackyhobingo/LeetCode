class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = re.match(r'[+-]?[0-9]+', str.strip())
        return 0 if not r else max(-2147483648, min(2147483647, int(r.group())))
