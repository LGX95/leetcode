"""Question: https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List

from util import print_vars


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs:
            while prefix and prefix != s[:len(prefix)]:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    output = Solution().longestCommonPrefix(strs)
    print_vars(strs, output)
