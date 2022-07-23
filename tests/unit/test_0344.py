from problems.problem_0344 import Solution

sol = Solution()


def test_case1():
    s = ["h", "e", "l", "l", "o"]
    sol.reverseString(s)
    assert s == ["o", "l", "l", "e", "h"]


def test_case2():
    s = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s)
    assert s == ["h", "a", "n", "n", "a", "H"]
