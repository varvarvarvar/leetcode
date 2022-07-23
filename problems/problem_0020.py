"""Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:

            if ch in pairs:
                stack.append(ch)
                continue

            if not stack:
                return False

            last_open = stack.pop()

            if ch != pairs[last_open]:
                return False

        return not stack
