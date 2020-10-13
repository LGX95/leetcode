"""Question: https://leetcode.com/problems/find-common-characters/
"""

from typing import List

from util import print_vars


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        cnt = Counter(A[0])
        for i in A:
            cnt &= Counter(i)
        return list(cnt.elements())


if __name__ == '__main__':
    a = ["bella", "label", "roller"]
    output = Solution().commonChars(a)
    print_vars(a, output)
