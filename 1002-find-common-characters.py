"""Question: https://leetcode.com/problems/find-common-characters/
"""

from typing import List

from util import print_vars


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        cnt = Counter(A[0])
        for i in A:
            ci = Counter(i)
            for c in cnt:
                cnt[c] = min(cnt[c], ci[c])
        res = []
        for i, c in cnt.items():
            res.extend([i] * c)
        return res


if __name__ == '__main__':
    a = ["bella", "label", "roller"]
    output = Solution().commonChars(a)
    print_vars(a, output)
