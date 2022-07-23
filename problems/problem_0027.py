"""Given an array nums and a value val,
remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length.
"""


class Solution:
    def __init__(self):
        self.nums = None

    def removeElement(self, nums, val, debug_mode=False) -> int:

        last_correct_idx = 0

        for nums_val in nums:

            if nums_val == val:
                continue

            nums[last_correct_idx] = nums_val
            last_correct_idx += 1

        if debug_mode:  # Sanity check
            self.nums = nums[:last_correct_idx]

        return last_correct_idx
