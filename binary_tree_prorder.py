# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder_traversal(self, root: TreeNode | None) -> List[int]:
        result = []
        def dfs(node: TreeNode | None):
            if not node:
                return
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return result
