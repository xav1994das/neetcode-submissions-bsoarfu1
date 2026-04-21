# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return (0,True)
            l,flag=dfs(node.left)
            if flag==False:
                return (-1,flag)
            r,flag=dfs(node.right)
            if flag==False:
                return (-1,flag)
            diff=abs(l-r)
            print("at node", node.val, "diff height",diff)
            if diff>1:
                isBalanced=False
            else:
                isBalanced=True
            return (1+max(l,r),isBalanced)
            
        x,y=dfs(root)
        return y