"""Given a 32-bit signed integer, reverse digits of an integer."""


class Solution:

    def reverse(self, x: int) -> int:

        if not x:
            return 0

        sign = 1 if x >= 0 else -1

        x = list(str(abs(x)))

        for i in range(len(x)//2):
            x[i], x[len(x)-i-1] = x[len(x)-i-1], x[i]

        x = int(''.join(x))
        x *= sign
        x *= -2**31 <= x <= 2**31 - 1

        return x


sol = Solution()

assert sol.reverse(-123) == -321
assert sol.reverse(120) == 21
assert sol.reverse(0) == 0
assert sol.reverse(1534236469) == 0
assert sol.reverse(1) == 1
