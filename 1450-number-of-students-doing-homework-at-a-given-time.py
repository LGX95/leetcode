"""Question: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/   # noqa
"""

from typing import List

from util import print_vars


class Solution:
    def busyStudent(
        self, startTime: List[int], endTime: List[int], queryTime: int
    ) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))


if __name__ == "__main__":
    startTime, endTime, queryTime = [1, 2, 3], [3, 2, 7], 4
    output = Solution().busyStudent(startTime, endTime, queryTime)
    print_vars(startTime, endTime, queryTime, output)
