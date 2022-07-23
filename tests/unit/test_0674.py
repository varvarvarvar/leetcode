from problems.problem_0674 import Solution

sol = Solution()


def test_case1():
    assert Solution().findLengthOfLCIS([1, 3, 5, 4, 7]) == 3


def test_case2():
    assert Solution().findLengthOfLCIS([2, 2, 2, 2, 2]) == 1
