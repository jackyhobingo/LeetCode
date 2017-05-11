class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        i_primes = [0] * len(primes)
        for i in range(1, n):
            min_ = 2 ** 31
            for j in range(len(primes)):
                i_primes[j] += ugly[i_primes[j]] * primes[j] == ugly[-1]
                min_ = min(ugly[i_primes[j]] * primes[j], min_)
            ugly.append(min_)
        return ugly[-1]
