from problems.problem_0027 import Solution

sol = Solution()


def test_case1():
    assert sol.removeElement([3, 2, 2, 3], 3, debug_mode=True) == 2
    assert sol.nums == [2, 2]


def test_case2():
    assert sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2, debug_mode=True) == 5
    assert sol.nums == [0, 1, 3, 0, 4]
