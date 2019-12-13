"""Given an array with n integers, your task is to check
if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1]
holds for every i (1 <= i < n).
"""

import unittest


class Solution:
    def checkPossibility(self, nums):

        res_sum = sum([nums[i] >= nums[i-1] for i in range(1, len(nums))])

        if res_sum < len(nums)-2:
            return False

        for i in range(1, len(nums)):

            if nums[i] >= nums[i-1]:
                continue

            if i == len(nums) - 1:
                nums_next = nums[i] + nums[i-1]
            else:
                nums_next = nums[i+1]

            if i == 1:
                nums_prev_prev = 0
            else:
                nums_prev_prev = nums[i-2]

            if nums[i]-nums_prev_prev < 1 and nums_next-nums[i-1] < 1:
                return False

        return True


class TestStringMethods(unittest.TestCase):

    def test_upper(self):

        sol = Solution()

        self.assertEqual(sol.checkPossibility([4, 2, 3]), True)
        self.assertEqual(sol.checkPossibility([4, 2, 1]), False)
        self.assertEqual(sol.checkPossibility([3, 4, 2, 3]), False)
        self.assertEqual(sol.checkPossibility([1]), True)
        self.assertEqual(sol.checkPossibility([1, 3, 2]), True)
        self.assertEqual(sol.checkPossibility([1, 1, 1]), True)
        self.assertEqual(sol.checkPossibility([1, 2, 4, 5, 3]), True)


if __name__ == '__main__':
    unittest.main()
