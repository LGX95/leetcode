"""Question: https://leetcode.com/problems/lemonade-change/
"""

from typing import List

from util import print_vars


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        in_hand = {5: 0, 10: 0, 20: 0}
        for i in bills:
            if i == 5:
                in_hand[i] += 1
            elif i == 10:
                if in_hand[5] < 1:
                    return False
                in_hand[5] -= 1
                in_hand[10] += 1
            elif i == 20:
                if in_hand[5] > 0 and in_hand[10] > 0:
                    in_hand[5] -= 1
                    in_hand[10] -= 1
                    in_hand[20] += 1
                elif in_hand[5] >= 3:
                    in_hand[5] -= 3
                    in_hand[20] += 1
                else:
                    return False
        return True


if __name__ == "__main__":
    bills = [5, 5, 5, 10, 20]
    output = Solution().lemonadeChange(bills)
    print_vars(bills, output)
