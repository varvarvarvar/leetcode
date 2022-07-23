from problems.problem_0028 import Solution

sol = Solution()


def test_case1():
    assert sol.strStr("aaa", "aaaa") == -1


def test_case2():
    assert sol.strStr("mississippi", "issip") == 4


def test_case3():
    assert sol.strStr("hello", "ll") == 2


def test_case4():
    assert sol.strStr("aaa", "aaa") == 0


def test_case5():
    assert sol.strStr("a", "a") == 0


def test_case6():
    assert sol.strStr("aaa", "aaa") == 0


def test_case7():
    assert sol.strStr("ba", "a") == 1


def test_case8():
    assert sol.strStr("aaaaa", "bba") == -1


def test_case9():
    assert sol.strStr("", "") == 0
