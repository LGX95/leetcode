"""Question: https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

from datastruct import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode,
                            headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a is not None else headB
            b = b.next if b is not None else headA
        return a
