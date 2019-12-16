"""Given an array nums and a value val,
remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed.
It doesn't matter what you leave beyond the new length."""


class Solution:

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def removeElement(self, nums, val, debug_mode=False) -> int:

        last_correct_idx = 0

        for i in range(len(nums)):

            if nums[i] == val:
                continue

            nums[last_correct_idx] = nums[i]
            last_correct_idx += 1

        if self.debug_mode:
            self.nums = nums[:last_correct_idx]

        return last_correct_idx


sol = Solution(debug_mode=True)

assert sol.removeElement([3, 2, 2, 3], 3) == 2
assert sol.nums == [2, 2]

assert sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
assert sol.nums == [0, 1, 3, 0, 4]
