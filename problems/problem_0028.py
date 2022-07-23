"""Return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

For the purpose of this problem, we will return 0 when needle is an empty string.

"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        if len(needle) == len(haystack):
            if needle == haystack:
                return 0
            return -1

        for i in range(len(haystack) - len(needle) + 1):

            first_j = i

            for j in range(len(needle)):

                if first_j == len(haystack):
                    break

                if haystack[first_j] != needle[j]:
                    break

                first_j += 1

                if first_j - i == len(needle):
                    return i

        return -1
