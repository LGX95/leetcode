"""Question: https://leetcode.com/problems/sum-of-even-numbers-after-queries/
"""

from typing import List

from util import print_vars


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        sum_even = sum(i for i in A if i % 2 == 0)
        for val, index in queries:
            previous = A[index]
            A[index] += val
            if A[index] % 2 == 0 and previous % 2 != 0:
                sum_even += A[index]
            if A[index] % 2 == 0 and previous % 2 == 0:
                sum_even += val
            if A[index] % 2 != 0 and previous % 2 == 0:
                sum_even -= previous
            res.append(sum_even)
        return res


if __name__ == "__main__":
    A, queries = [1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]
    output = Solution().sumEvenAfterQueries(A, queries)
    print_vars(A, queries, output)
