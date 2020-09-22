"""Question: https://leetcode.com/problems/plus-one/
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = True
        for i in reversed(range(len(digits))):
            if plus:
                digits[i] += 1
            if digits[i] >= 10:
                plus = True
                digits[i] %= 10
            else:
                return digits
        if plus:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(f'digits: {digits}')
    output = Solution().plusOne(digits)
    print(f'output: {output}')
