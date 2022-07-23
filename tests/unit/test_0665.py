from problems.problem_0665 import Solution

sol = Solution()


def test_case1():
    assert sol.checkPossibility([4, 2, 3])


def test_case2():
    assert not sol.checkPossibility([4, 2, 1])


def test_case3():
    assert not sol.checkPossibility([3, 4, 2, 3])


def test_case4():
    assert sol.checkPossibility([1])


def test_case5():
    assert sol.checkPossibility([1, 3, 2])


def test_case6():
    assert sol.checkPossibility([1, 1, 1])


def test_case7():
    assert sol.checkPossibility([1, 2, 4, 5, 3])
