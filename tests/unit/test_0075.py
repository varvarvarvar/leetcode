from problems.problem_0075 import Solution


def test_case1():
    colors = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(colors)
    assert colors == [0, 0, 1, 1, 2, 2]
