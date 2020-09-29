"""Question: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from typing import List

from datastruct import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def output(root, result):
            if root:
                result = output(root.left, result)
                result.append(root.val)
                result = output(root.right, result)
            return result

        result = []
        return output(root, result)
