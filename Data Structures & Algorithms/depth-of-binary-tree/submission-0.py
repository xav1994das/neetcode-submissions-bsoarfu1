# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        t=root
        if not t:
            return 0

        l=1+self.maxDepth(t.left)
        r=1+self.maxDepth(t.right)
        return max(l,r)