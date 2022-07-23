from problems.problem_0771 import Solution

sol = Solution()


def test_case1():
    assert Solution().numJewelsInStones(J="aA", S="aAAbbbb") == 3


def test_case2():
    assert Solution().numJewelsInStones(J="z", S="ZZ") == 0
