from problems.problem_0009 import Solution

sol = Solution()


def test_case1():
    assert not sol.isPalindrome(9223372036854775807)


def test_case2():
    assert not sol.isPalindrome(12822)


def test_case3():
    assert not sol.isPalindrome(-2147447412)


def test_case4():
    assert sol.isPalindrome(121)
