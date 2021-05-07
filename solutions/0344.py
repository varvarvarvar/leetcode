"""Write a function that reverses a string.
The input string is given as an array of characters s.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Do not return anything, modify s in-place instead.
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:

        i, j = 0, len(s) - 1

        while i <= j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == "__main__":

    sol = Solution()

    s = ["h", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]

    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
