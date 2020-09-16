"""Question: https://leetcode.com/problems/validate-binary-search-tree/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid_bst_recu(root, low, high):
            if root is None:
                return True
            return (low < root.val < high
                    and is_valid_bst_recu(root.left, low, root.val)
                    and is_valid_bst_recu(root.right, root.val, high))

        return is_valid_bst_recu(root, float('-inf'), float('inf'))
