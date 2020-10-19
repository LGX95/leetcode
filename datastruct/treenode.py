#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" TreeNode data struct
some implement ref:
  * https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python # noqa
"""

from __future__ import annotations
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def height(self):
        def recur(root):
            return 1 + max(recur(root.left), recur(root.right)) if root else -1

        return recur(self)

    @classmethod
    def from_list(cls, array: List[Optional[int]]) -> TreeNode:
        if not array:
            return None
        nodes = [cls(i) if i is not None else None for i in array]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root

    @classmethod
    def deserialize(cls, string: str):
        array = [
            None if i == "null" else int(i) for i in string.strip("[]{}").split(",")
        ]
        return cls.from_list(array)

    def to_list(self):
        result = [self.val]
        kids = [self.left, self.right]

        # why not any(kids), in case the value is 0
        while kids and any(i is not None for i in kids):
            node = kids.pop(0)
            if node:
                result.append(node.val)
                kids.append(node.left)
                kids.append(node.right)
            else:
                result.append(node)
        return result


if __name__ == "__main__":
    root = [1, None, 2, 3]
    node = TreeNode.from_list(root)
    print(root, node.to_list())
    print(node)

    root = [2, 1, 3]
    node = TreeNode.from_list(root)
    print(root, node.to_list())
    print(node)

    root = [1]
    node = TreeNode.from_list(root)
    print(root, node.to_list())

    root = [1, None, 2]
    node = TreeNode.from_list(root)
    print(root, node.to_list())

    root = "[3,5,1,6,2,0,8,null,null,7,4]"
    node = TreeNode.deserialize(root)
    print(root, node.to_list())
