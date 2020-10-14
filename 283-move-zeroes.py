"""Question: https://leetcode.com/problems/move-zeroes/
"""

from typing import List
from util import print_vars


class Solution:
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
