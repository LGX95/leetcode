"""Question: https://leetcode.com/problems/powx-n/
"""

from util import print_vars


class Solution:
    def my_pow_binary(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return res

    def my_pow_binary_bit(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

    def myPow(self, x: float, n: int) -> float:
        return x**n


if __name__ == '__main__':
    x, n = 2.0, 10
    output = Solution().myPow(x, n)
    print_vars(x, n, output)

    x, n = 2.0, 10
    output = Solution().my_pow_binary(x, n)
    print_vars(x, n, output)

    x, n = 2.0, 10
    output = Solution().my_pow_binary_bit(x, n)
    print_vars(x, n, output)
