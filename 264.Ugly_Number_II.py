class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly_array = [1]
        i2 = i3 = i5 = 0
        for i in range(1, n):
            i2 += ugly_array[i2] * 2 == ugly_array[-1]
            i3 += ugly_array[i3] * 3 == ugly_array[-1]
            i5 += ugly_array[i5] * 5 == ugly_array[-1]
            ugly_array.append(min(ugly_array[i2] * 2, ugly_array[i3] * 3, ugly_array[i5] * 5))
        return ugly_array[-1]
