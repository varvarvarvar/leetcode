"""Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        id2val = {}
        val2id = {}

        for i, num in enumerate(nums):
            id2val[i] = num
            val2id[num] = i

        for i, num in enumerate(nums):
            if target - num in val2id and i != val2id[target - num]:
                return i, val2id[target - num]


assert Solution().twoSum([2, 7, 11, 15], 9) == (0, 1)
