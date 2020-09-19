"""Question: https://leetcode.com/problems/reverse-linked-list/
"""

from datastruct import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        while head:
            # nxt = head.next
            # head.next = previous
            # previous = head
            # head = nxt
            head.next, previous, head = previous, head, head.next
        return previous


if __name__ == '__main__':
    head = ListNode.from_list([1, 2, 3, 4, 5])
    print(f'head: {head}')
    output = Solution().reverseList(head)
    print(f'output: {output}')
