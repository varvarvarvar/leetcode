from problems.problem_0189 import Solution

sol = Solution()


def test_case1():
    nums = []
    Solution().rotate(nums, 1)
    assert nums == []


def test_case2():
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
