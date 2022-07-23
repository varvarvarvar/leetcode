"""Given a sorted array consisting of only integers where every element appears twice except
for one element which appears once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""


class Solution:
    def singleNonDuplicate(self, nums):

        end = len(nums)
        start = 0
        mid = end // 2

        while start < mid:

            m = (start + mid) // 2

            if nums[2 * m] != nums[2 * m + 1]:
                mid = m
            else:
                start = m + 1

        return nums[2 * start]
