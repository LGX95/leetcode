"""Question: https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

from typing import List

from datastruct import Node


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def output(root, result):
            if root:
                for node in root.children:
                    output(node, result)
                result.append(root.val)
            return result

        result = []
        return output(root, result)
