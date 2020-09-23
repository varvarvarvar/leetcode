from typing import List


class Solution:
    """Given an array nums of n integers,
    are there elements a, b, c in nums such that a + b + c = 0?

    Find all unique triplets in the array which gives the sum of zero.
    Notice that the solution set must not contain duplicate triplets.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        target = 0
        res = []

        for i in range(len(nums) - 2):

            idx0, idx1 = i + 1, len(nums) - 1

            while idx0 < idx1:

                cur_sum = nums[i] + nums[idx0] + nums[idx1]

                if cur_sum == target:
                    res.append((nums[i], nums[idx0], nums[idx1]))
                    idx0 += 1
                    idx1 -= 1
                elif cur_sum < target:
                    idx0 += 1
                else:
                    idx1 -= 1

        return list(set(res))


sol = Solution()
assert sol.threeSum([-1, 0, 1, 2, -1, -4]) == [(-1, 0, 1), (-1, -1, 2)]
assert sol.threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]) == [
    (-3, -1, 4), (-1, 0, 1), (-4, 1, 3),
    (-2, 0, 2), (-1, -1, 2), (-3, 0, 3),
    (-4, 0, 4), (-2, -1, 3), (-3, 1, 2)
    ]
