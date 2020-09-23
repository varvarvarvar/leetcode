from typing import List


class Solution:
    """Given n non-negative integers a1, a2, ..., an,
    where each represents a point at coordinate (i, ai),
    n vertical lines are drawn
    such that the two endpoints of line i is at (i, ai)
    and (i, 0).

    Find two lines, which together with x-axis forms a container,
    such that the container contains the most water.

    """

    def maxArea(self, height: List[int]) -> int:

        idx0, idx1 = 0, len(height) - 1
        max_area = 0

        while idx0 < idx1:

            cur_area = min(height[idx0], height[idx1]) * abs(idx1 - idx0)
            max_area = max(max_area, cur_area)

            if height[idx0] < height[idx1]:
                idx0 += 1
            else:
                idx1 -= 1

        return max_area


sol = Solution()

assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert sol.maxArea([3, 9, 3, 4, 7, 2, 12, 6]) == 45
assert sol.maxArea([1, 2]) == 1
assert sol.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24
assert sol.maxArea([1, 1]) == 1
