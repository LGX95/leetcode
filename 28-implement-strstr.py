"""Question: https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == "" and needle == "":
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = "hello"
    needle = "ll"
    output = Solution().strStr(haystack, needle)
    print(f'haystack: {haystack}, needle: {needle}, output: {output}')
    assert output == 2
