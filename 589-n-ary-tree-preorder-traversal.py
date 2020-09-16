"""Question: https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""

from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self,
                 val: Optional[int] = None,
                 children: Optional[List[Node]] = None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def recur(root, result):
            if not root:
                return
            result.append(root.val)
            if root.children:
                for i in root.children:
                    recur(i, result)

        result = []
        recur(root, result)
        return result

    def preorder_iter(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        stack.append(root)
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            result.append(curr.val)
            if curr.children:
                for i in curr.children[::-1]:
                    stack.append(i)
        return result
