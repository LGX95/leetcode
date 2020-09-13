"""Question: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from __future__ import annotations  # for ListNode type hint
from typing import List, Optional


class ListNode:
    """Definition for singly-linked list.
    """
    def __init__(self, val: int = 0, nxt: Optional[ListNode] = None):
        self.val = val
        self.next = nxt

    def __str__(self):
        return f'{self.val} -> {self.next}'

    @classmethod
    def from_list(cls, array: List[int]) -> ListNode:
        curr = dummy = cls()
        for i in array:
            curr.next = cls(i)
            curr = curr.next
        return dummy.next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


if __name__ == '__main__':
    head = ListNode.from_list([1, 1, 2])
    print(f'head: {head}')
    output = Solution().deleteDuplicates(head)
    print(f'output: {output}')

    head = ListNode.from_list([1, 1, 2, 3, 3])
    print(f'head: {head}')
    output = Solution().deleteDuplicates(head)
    print(f'output: {output}')
