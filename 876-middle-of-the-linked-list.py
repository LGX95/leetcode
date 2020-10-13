"""Question: https://leetcode.com/problems/middle-of-the-linked-list/
"""

from datastruct import ListNode
from util import print_vars


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    head = ListNode.from_list([1, 2, 3, 4, 5])
    output = Solution().middleNode(head)
    print_vars(head, output)

    head = ListNode.from_list([1, 2, 3, 4, 5, 6])
    output = Solution().middleNode(head)
    print_vars(head, output)
