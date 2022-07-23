"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red,
white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""


class Solution:
    def merge(self, left_part, right_part, a):
        i = 0
        j = 0
        k = 0

        while i < len(left_part) and j < len(right_part):
            if left_part[i] <= right_part[j]:
                a[k] = left_part[i]
                i += 1
            else:
                a[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            a[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            a[k] = right_part[j]
            j += 1
            k += 1

    def merge_sort(self, a):
        if len(a) > 1:
            mid_ind = len(a) // 2

            left_part = a[:mid_ind]
            right_part = a[mid_ind:]

            self.merge_sort(left_part)
            self.merge_sort(right_part)

            self.merge(left_part, right_part, a)

    def sortColors(self, nums):
        self.merge_sort(nums)
