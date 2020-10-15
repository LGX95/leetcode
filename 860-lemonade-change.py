"""Question: https://leetcode.com/problems/lemonade-change/
"""

from typing import List

from util import print_vars


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                five -= 1
                ten += 1
            elif ten > 0:  # i = 20
                five -= 1
                ten -= 1
            else:  # i = 20 and no 10 in hand
                five -= 3

            if five < 0:
                return False
        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    output = Solution().lemonadeChange(bills)
    print_vars(bills, output)
