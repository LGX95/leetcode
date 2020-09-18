"""Question: https://leetcode.com/problems/linked-list-cycle/
"""

from datastruct import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while slow is not None and fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False


if __name__ == '__main__':
    head = ListNode.from_list([3, 2, 0, -4])
    print(Solution().hasCycle(head))
