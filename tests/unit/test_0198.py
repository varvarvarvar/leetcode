from problems.problem_0198 import Solution

sol = Solution()


def test_case1():
    assert sol.rob([2, 1, 1, 2]) == 4


def test_case1():
    assert sol.rob([]) == 0


def test_case1():
    assert sol.rob([2, 7, 9, 3, 1]) == 12


def test_case1():
    assert sol.rob([1, 2, 3, 1]) == 4
