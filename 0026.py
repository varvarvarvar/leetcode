"""Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this
by modifying the input array in-place with O(1) extra memory.

It doesn't matter what you leave beyond the returned length."""


class Solution:

    def removeDuplicates(self, nums, debug_mode=False) -> int:

        len_nums = len(nums)

        if len_nums < 2:
            return len_nums

        last_correct_idx = 0

        for i in range(1, len_nums):
            if nums[i] == nums[last_correct_idx]:
                continue

            nums[last_correct_idx + 1] = nums[i]
            last_correct_idx += 1

        if debug_mode:  # Sanity check
            self.nums = nums[: last_correct_idx + 1]

        return last_correct_idx + 1


sol = Solution()

assert sol.removeDuplicates(
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    debug_mode=True
) == 5
assert sol.nums == [0, 1, 2, 3, 4]

assert sol.removeDuplicates([1, 1, 2], debug_mode=True) == 2
assert sol.nums == [1, 2]

assert sol.removeDuplicates([]) == 0
