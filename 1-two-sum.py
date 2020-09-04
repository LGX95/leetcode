"""Question: https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {n: i for i, n in enumerate(nums)}
        for i, n in enumerate(nums):
            if target - n in nums_idx and i != nums_idx[target - n]:
                return [i, nums_idx[target - n]]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    output = Solution().twoSum(nums, target)
    print(output)
