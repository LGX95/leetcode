"""Question: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from typing import List

from util import print_vars


class Solution:
    def intersect_two_pointer(self, nums1: List[int],
                              nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted(nums1), sorted(nums2)
        p1, p2 = 0, 0
        res = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                p1 += 1
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            else:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
        return res

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        nums1_cnt = Counter(nums1)
        res = []
        for i in nums2:
            if nums1_cnt[i] > 0:
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

    nums1, nums2 = [1, 2, 2, 1], [2, 2]
    output = Solution().intersect_two_pointer(nums1, nums2)
    print_vars(nums1, nums2, output)

    nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]
    output = Solution().intersect_two_pointer(nums1, nums2)
    print_vars(nums1, nums2, output)
