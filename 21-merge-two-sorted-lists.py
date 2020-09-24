"""Question: https://leetcode.com/problems/merge-two-sorted-lists/
"""

from datastruct import ListNode


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
