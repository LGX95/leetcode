"""Question: https://leetcode.com/problems/delete-node-in-a-linked-list/
"""

from datastruct import ListNode
from util import print_vars


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    head = ListNode.from_list([4, 5, 1, 9])
    node = head.next
    print_vars(head, node)
    print('delete node: ', node)
    Solution().deleteNode(node)
    print_vars(head, node)
