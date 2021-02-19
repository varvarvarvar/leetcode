"""Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        if len(set(strs)) == 1:
            return strs[0]
        prefix = []
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                return "".join(prefix)
            prefix.append(chars[0])
        return "".join(prefix)


sol = Solution()

assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
assert sol.longestCommonPrefix(["aca", "cba"]) == ""
assert sol.longestCommonPrefix(["ab", "ab"]) == "ab"
assert sol.longestCommonPrefix([]) == ""
assert sol.longestCommonPrefix(["", "b"]) == ""
