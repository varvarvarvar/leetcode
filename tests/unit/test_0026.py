from problems.problem_0026 import Solution

sol = Solution()


def test_case1():
    assert sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], debug_mode=True) == 5
    assert sol.nums == [0, 1, 2, 3, 4]


def test_case2():
    assert sol.removeDuplicates([1, 1, 2], debug_mode=True) == 2
    assert sol.nums == [1, 2]


def test_case3():
    assert sol.removeDuplicates([]) == 0
