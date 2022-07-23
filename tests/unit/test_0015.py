from problems.problem_0015 import Solution

sol = Solution()


def test_case1():
    assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [(-1, 0, 1), (-1, -1, 2)]


def test_case2():
    assert sol.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [
        (-3, -1, 4),
        (-1, 0, 1),
        (-4, 1, 3),
        (-2, 0, 2),
        (-1, -1, 2),
        (-3, 0, 3),
        (-4, 0, 4),
        (-2, -1, 3),
        (-3, 1, 2),
    ]
