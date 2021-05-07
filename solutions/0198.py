from typing import List


class Solution:
    """You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed,
    the only constraint stopping you from robbing each of them
    is that adjacent houses have security system connected and
    it will automatically contact the police
    if two adjacent houses were broken into
    on the same night.

    Given a list of non-negative integers
    representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight
    without alerting the police.
    """

    def rob(self, nums: List[int]) -> int:

        rob0, rob1 = 0, 0

        for num in nums:

            current = max(rob1, rob0 + num)

            rob0 = rob1
            rob1 = current

        return max(rob0, rob1)


sol = Solution()

assert sol.rob([2, 1, 1, 2]) == 4
assert sol.rob([]) == 0
assert sol.rob([2, 7, 9, 3, 1]) == 12
assert sol.rob([1, 2, 3, 1]) == 4
