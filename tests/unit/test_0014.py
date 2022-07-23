from problems.problem_0014 import Solution

sol = Solution()


def test_case1():
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_case2():
    assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_case3():
    assert sol.longestCommonPrefix(["aca", "cba"]) == ""


def test_case4():
    assert sol.longestCommonPrefix(["ab", "ab"]) == "ab"


def test_case5():
    assert sol.longestCommonPrefix([]) == ""


def test_case6():
    assert sol.longestCommonPrefix(["", "b"]) == ""
