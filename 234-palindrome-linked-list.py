"""Question: https://leetcode.com/problems/palindrome-linked-list/
"""

from datastruct import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        reverse = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            head.next, reverse, head = reverse, head, head.next

        mid = head.next if fast else head
        print(mid)
        print(reverse)

        while reverse and mid:
            if reverse.val != mid.val:
                return False
            reverse = reverse.next
            mid = mid.next
        if reverse is None and mid is None:
            return True
        return False


if __name__ == '__main__':
    head = ListNode.from_list([1, 2, 2, 1])
    print(f'head: {head}')
    output = Solution().isPalindrome(head)
    print(f'output: {output}')
