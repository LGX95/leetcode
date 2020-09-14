from datastruct import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pre = dummy = ListNode()
        dummy.next = curr = head
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next

        return dummy.next


if __name__ == '__main__':
    head = ListNode.from_list([1, 2, 6, 3, 4, 5, 6])
    val = 6
    print(f'head: {head}\tval: {val}')
    output = Solution().removeElements(head, val)
    print(f'output: {output}')
