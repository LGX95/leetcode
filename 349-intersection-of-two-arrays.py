"""Question: https://leetcode.com/problems/intersection-of-two-arrays/
"""

from typing import List

from util import print_vars


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    output = Solution().intersection(nums1, nums2)
    print_vars(nums1, nums2, output)

    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    output = Solution().intersection(nums1, nums2)
    print_vars(nums1, nums2, output)
