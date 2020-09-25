"""Question: https://leetcode.com/problems/climbing-stairs/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    for i in range(90):
        print(i, Solution().climbStairs(i))
