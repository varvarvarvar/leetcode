"""Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
"""


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        k = k % len(nums)
        n = len(nums)

        for i in range(k):
            tmp = nums[i]
            nums[i] = nums[n - k + i]
            nums[n - k + i] = tmp

        for i in range(k, n - 1):
            tmp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = tmp
