from problems.problem_0020 import Solution

sol = Solution()


def test_case1():
    assert Solution().isValid("()")


def test_case2():
    assert Solution().isValid("()[]{}")


def test_case3():
    assert not Solution().isValid("(]")


def test_case4():
    assert not Solution().isValid("([)]")


def test_case5():
    assert Solution().isValid("{[]}")


def test_case6():
    assert Solution().isValid("(((((())))))")


def test_case7():
    assert Solution().isValid("{}{}()[]")
