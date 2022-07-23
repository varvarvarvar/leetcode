from problems.problem_0007 import Solution

sol = Solution()


def test_case1():
    assert sol.reverse(-123) == -321


def test_case2():
    assert sol.reverse(120) == 21


def test_case3():
    assert sol.reverse(0) == 0


def test_case4():
    assert sol.reverse(1534236469) == 0


def test_case5():
    assert sol.reverse(1) == 1
