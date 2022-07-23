"""Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai),
n vertical lines are drawn
such that the two endpoints of line i is at (i, ai)
and (i, 0).

Find two lines, which together with x-axis forms a container,
such that the container contains the most water.
"""

from typing import List


class Solution:
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
