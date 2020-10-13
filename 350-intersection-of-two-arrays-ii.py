"""Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from typing import List

from util import print_vars


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        nums1_cnt = defaultdict(int)
        res = []
        for i in nums1:
            nums1_cnt[i] += 1
        for i in nums2:
            if nums1_cnt.get(i) and nums1_cnt.get(i) > 0:
                res.append(i)
                nums1_cnt[i] -= 1
        return res


if __name__ == '__main__':
    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    output = Solution().intersect(nums1, nums2)
    print_vars(nums1, nums2, output)

    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    output = Solution().intersect(nums1, nums2)
    print_vars(nums1, nums2, output)
