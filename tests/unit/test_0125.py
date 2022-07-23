from problems.problem_0125 import Solution

sol = Solution()


def test_case1():
    assert Solution().isPalindrome("a,ba")


def test_case2():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")


def test_case3():
    assert not (Solution().isPalindrome("race a car"))


def test_case4():
    assert Solution().isPalindrome("")
