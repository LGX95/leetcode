"""Question: https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

from typing import List

from datastruct import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def output(root, result):
            if root:
                result.append(root.val)
                result = output(root.left, result)
                result = output(root.right, result)
            return result

        result = []
        return output(root, result)
