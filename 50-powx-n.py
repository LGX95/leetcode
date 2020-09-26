"""Question: https://leetcode.com/problems/powx-n/
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n


if __name__ == '__main__':
    x, n = 2.0, 10
    output= Solution().myPow(x, n)
    print(f'x: {x} n: {n} output: {output}')
