"""Description:

Count the number of prime numbers less than a non-negative number, n.

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0

        sieve = [True] * n
        sieve[0], sieve[1] = False, False

        for i in range(2, int(n**0.5)+1):

            if not sieve[i]:
                continue

            sieve[i*i:n:i] = [False] * len(sieve[i * i:n:i])

        return sum(sieve)


assert Solution().countPrimes(999983) == 78497
