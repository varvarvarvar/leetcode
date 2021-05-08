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


if __name__ == "__main__":

    sol = Solution()

    assert sol.strStr("aaa", "aaaa") == -1
    assert sol.strStr("mississippi", "issip") == 4
    assert sol.strStr("hello", "ll") == 2
    assert sol.strStr("aaa", "aaa") == 0
    assert sol.strStr("a", "a") == 0
    assert sol.strStr("aaa", "aaa") == 0
    assert sol.strStr("ba", "a") == 1
    assert sol.strStr("aaaaa", "bba") == -1
    assert sol.strStr("", "") == 0
