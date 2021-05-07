"""Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        i = 0
        j = len(s) - 1

        if not s:
            return True

        for _ in range(len(s)):

            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            else:
                if not s[i].isalnum():
                    i += 1
                if not s[j].isalnum():
                    j -= 1

        return True


assert Solution().isPalindrome("a,ba")
assert Solution().isPalindrome("A man, a plan, a canal: Panama")
assert not (Solution().isPalindrome("race a car"))
assert Solution().isPalindrome("")
