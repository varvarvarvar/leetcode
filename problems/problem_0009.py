"""Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.
"""


class Solution:
    def get_digit(self, num, i):
        return (num % 10 ** (i + 1) - num % 10**i) / 10**i

    def isPalindrome(self, x):

        if x < 0:
            return False

        for i in range(20):
            if x < 10**i:
                num_digits = i
                break

        mid = round((num_digits + 1) // 2)

        for i in range(mid):
            d_last = self.get_digit(x, i)
            d_first = self.get_digit(x, num_digits - i - 1)

            if d_last != d_first:
                return False

        return True
