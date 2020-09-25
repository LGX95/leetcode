"""Question: https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from datastruct import ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode()
        while head and head.next:
            tmp = head.next.next
            curr.next = head.next
            curr.next.next = head
            head = tmp
            curr = curr.next.next
        curr.next = head
        return dummy.next


if __name__ == '__main__':
    head = ListNode.from_list([1, 2, 3, 4])
    print(f'head: {head}')
    output = Solution().swapPairs(head)
    print(f'output: {output}')
