"""Question: https://leetcode.com/problems/move-zeroes/
"""

from typing import List
from util import print_vars


class Solution:
    def move_zeros_two_pointer(self, nums: List[int]) -> None:
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1
            fast += 1

    def move_zeros_save_non_zero(self, nums: List[int]) -> None:
        """currently fastest
        """
        tmp = [n for n in nums if n != 0]
        for i in range(len(nums)):
            if i < len(tmp):
                nums[i] = tmp[i]
            else:
                nums[i] = 0

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i + 1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print_vars(nums)
    Solution().moveZeroes(nums)
    print_vars(nums)

    nums = [0, 1, 0, 3, 12]
    print_vars(nums)
    Solution().move_zeros_save_non_zero(nums)
    print_vars(nums)

    nums = [0, 1, 0, 3, 12]
    print_vars(nums)
    Solution().move_zeros_two_pointer(nums)
    print_vars(nums)
