"""Question: https://leetcode.com/problems/remove-element/
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                del nums[i]
        return len(nums)


if __name__ == '__main__':
    nums = [3,2,2,3]
    val = 3
    length = Solution().removeElement(nums, val)
    print(f'len: {len(nums)}')
    print(f'nums: {nums}')
