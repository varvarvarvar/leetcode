from problems.problem_0540 import Solution

sol = Solution()


def test_case1():
    assert Solution().singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2


def test_case2():
    assert Solution().singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10
