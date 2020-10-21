"""Question: https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

from datastruct import TreeNode
from util import print_vars


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left and right:
            return min(left, right) + 1
        else:
            return left + right + 1


if __name__ == "__main__":
    root = TreeNode.deserialize("[3,9,20,null,null,15,7]")
    output = Solution().minDepth(root)
    print_vars(root, output)
