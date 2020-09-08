"""Question: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            '[': ']',
            '{': '}',
            '(': ')',
        }
        for i in s:
            if i in match:
                stack.append(i)
            elif len(stack) == 0 or match.get(stack.pop()) != i:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    s = '()'
    output = Solution().isValid(s)
    print(f's: {s}\t output: {output}')

    s = '()[]{}'
    output = Solution().isValid(s)
    print(f's: {s}\t output: {output}')

    s = '(]'
    output = Solution().isValid(s)
    print(f's: {s}\t output: {output}')

    s = '([)]'
    output = Solution().isValid(s)
    print(f's: {s}\t output: {output}')

    s = '{[]}'
    output = Solution().isValid(s)
    print(f's: {s}\t output: {output}')
