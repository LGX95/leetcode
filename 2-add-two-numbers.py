"""Question: https://leetcode.com/problems/add-two-numbers/
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode()
        carry = 0
        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            curr.next = ListNode(val % 10)
            carry = val // 10
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode.from_list([2, 4, 3])
    l2 = ListNode.from_list([5, 6, 4])
    print(f'l1: {l1}\nl2: {l2}')
    output = Solution().addTwoNumbers(l1, l2)
    print(f'output: {output}')
