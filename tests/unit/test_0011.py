from problems.problem_0011 import Solution

sol = Solution()


def test_case1():
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_case2():
    assert sol.maxArea([3, 9, 3, 4, 7, 2, 12, 6]) == 45


def test_case3():
    assert sol.maxArea([1, 2]) == 1


def test_case4():
    assert sol.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24


def test_case5():
    assert sol.maxArea([1, 1]) == 1
