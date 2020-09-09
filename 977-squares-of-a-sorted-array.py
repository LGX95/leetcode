"""Question: https://leetcode.com/problems/squares-of-a-sorted-array/
"""

from typing import List


class Solution:
    def sortedSquares_less_code(self, A: List[int]) -> List[int]:
        """It is faster the solution 2
        """
        return sorted(map(lambda x: x * x, A))

    # solution 2
    def sortedSquares(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        result = [0 for _ in range(len(A))]
        pos = len(A) - 1
        while left <= right:
            l_sq = A[left] ** 2
            r_sq = A[right] ** 2
            if l_sq > r_sq:
                result[pos] = l_sq
                left += 1
            else:
                result[pos] = r_sq
                right -= 1
            pos -= 1
        return result


if __name__ == '__main__':
    A = [-4, -1, 0, 3, 10]
    output = Solution().sortedSquares(A)
    print(f'A: {A}\toutput: {output}')
