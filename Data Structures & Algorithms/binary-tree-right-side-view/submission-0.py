# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return res
        dq=deque()
        dq.append(root)
        while dq:
            p=dq[-1]
            for _ in range(len(dq)):
                x=dq.popleft()
                if x.left:
                    dq.append(x.left)
                if x.right:
                    dq.append(x.right)
            res.append(p.val)
        return res
