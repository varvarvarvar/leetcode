from problems.problem_0657 import Solution

sol = Solution()


def test_case1():
    assert Solution().judgeCircle("UD")


def test_case2():
    assert not Solution().judgeCircle("LL")
