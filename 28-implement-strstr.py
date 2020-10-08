"""Question: https://leetcode.com/problems/implement-strstr/
"""

from util import print_vars


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    output = Solution().strStr(haystack, needle)
    print_vars(haystack, needle, output)
    assert output == 2
