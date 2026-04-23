# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0
        self.root=root
        maxi=-101
        def dfs(node,maxi):
            
            if node.val>=self.root.val and node.val>=maxi:
                self.res+=1
                maxi=node.val
            print("node val", node.val,"maxi",maxi,"res", self.res)
            if node.left:
                l=dfs(node.left,maxi)
            if node.right:
                r=dfs(node.right,maxi)
            return
        dfs(root,maxi)
        return self.res
