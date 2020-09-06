"""Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(1, len(nums)):
            if nums[cnt] != nums[i]:
                cnt += 1
                nums[cnt] = nums[i]

        return cnt + 1


if __name__ == '__main__':
    nums = [1, 1, 2]
    length = Solution().removeDuplicates(nums)
    print(f'len: {length}')
    print(f'nums: {nums}')
