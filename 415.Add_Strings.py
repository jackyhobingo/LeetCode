class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        d = {
            '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9
        }
        ans = ''
        if len(num1) > len(num2):
            num2 = (len(num1) - len(num2)) * "0" + num2
        else:
            num1 = (len(num2) - len(num1)) * "0" + num1
        carry = 0
        for i in range(len(num1)-1, -1, -1):
            a = d[num1[i]] + d[num2[i]] + carry
            carry = a > 9
            ans += str(a % 10)
        if carry:
            ans += str(int(carry))
        return ans[::-1]
