# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi=float('-inf')
        def dfs(node):
            nonlocal maxi
            if not node:
                return 0
            leftsum=dfs(node.left)
            rightsum=dfs(node.right)
            if leftsum<0:
                leftsum=0
            if rightsum<0:
                rightsum=0
            maxi=max(maxi, leftsum+rightsum+node.val)
            return max(leftsum, rightsum)+node.val
        dfs(root)
        return maxi