"""Question: https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        max_area = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    output = Solution().max_area(height)
    print(f'height: {height}\noutput: {output}')
