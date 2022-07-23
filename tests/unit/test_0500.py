from problems.problem_0500 import Solution

sol = Solution()


def test_case1():
    assert not Solution().findWords(["qwwewm"])


def test_case2():
    assert Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) == [
        "Alaska",
        "Dad",
    ]
