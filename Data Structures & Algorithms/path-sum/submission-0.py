# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.sum1=0
        def dfs(node, remaining):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return node.val==remaining
            l=dfs(node.left,remaining-node.val)
            r=dfs(node.right, remaining-node.val)
            return l or r

        return dfs(root, targetSum)