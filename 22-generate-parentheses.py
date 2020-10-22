"""Question: https://leetcode.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(par):
            if len(par) == n * 2:
                if is_valid(par):
                    res.append(''.join(par))
            else:
                par.append('(')
                generate(par)
                par.pop()
                par.append(')')
                generate(par)
                par.pop()

        def is_valid(par):
            ret = 0
            for i in par:
                if i == '(':
                    ret += 1
                else:
                    ret -= 1
                if ret < 0:
                    return False
            return ret == 0

        generate([])
        return res


if __name__ == '__main__':
    for i in range(1, 5):
        print(f'{i}: {Solution().generateParenthesis(i)}')
