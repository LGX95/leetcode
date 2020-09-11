"""Question: https://leetcode.com/problems/merge-two-sorted-lists/
"""


class ListNode:
    """Definition for singly-linked list.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'{self.val} -> {self.next}'

    @classmethod
    def from_list(cls, array):
        curr = dummy = cls()
        for i in array:
            curr.next = cls(i)
            curr = curr.next
        return dummy.next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = dummy = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next


if __name__ == '__main__':
    l1 = ListNode.from_list([1, 2, 4])
    l2 = ListNode.from_list([1, 3, 4])
    print(f'l1: {l1}\nl2: {l2}')
    output = Solution().mergeTwoLists(l1, l2)
    print(f'output: {output}\n')
