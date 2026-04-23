# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        h=float('inf')
        l=float('-inf')
        
        
        def isValid(node, l,h):
            if node is None:
                return True
            v=node.val
            if l<v and v<h:
                left=isValid(node.left,l,v)
                right=isValid(node.right,v,h)
                return left and right
            else:
                return False
        return isValid(root,l,h)