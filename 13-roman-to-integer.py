"""Question: https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        previous = float('-inf')
        result = 0
        for i in reversed(s):
            to_int = symbol[i]
            if to_int < previous:
                result -= to_int
            else:
                result += to_int
            previous = to_int
        return result


if __name__ == '__main__':
    s = 'MCMXCIV'
    output = Solution().romanToInt(s)
    print(f's: {s}\noutput: {output}')
