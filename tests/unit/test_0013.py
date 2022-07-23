from problems.problem_0013 import Solution

sol = Solution()


def test_case1():
    assert sol.romanToInt("IX") == 9


def test_case2():
    assert sol.romanToInt("LVIII") == 58


def test_case3():
    assert sol.romanToInt("MCMXCIV") == 1994
