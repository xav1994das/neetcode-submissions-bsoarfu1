# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot and root.val==subRoot.val:
            p=self.isSameTree(root, subRoot)
            print(p, root.val, subRoot.val)
            if p==True:
                return p
        if root:
            print(root.val, subRoot.val)
            l=self.isSubtree(root.left,subRoot)
            r=self.isSubtree(root.right,subRoot)
            return (l or r)
        return False
    
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        if t1 and t2:
            if t1.val==t2.val:
                l=self.isSameTree(t1.left,t2.left)
                r=self.isSameTree(t1.right,t2.right)

                return (l and r)
        return False