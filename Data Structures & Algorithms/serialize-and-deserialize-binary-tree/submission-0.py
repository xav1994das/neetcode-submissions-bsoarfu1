# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res=""
        dq=deque()
        dq.append(root)
        res+=str(root.val)+","
        while dq:
            p=dq.popleft()
            l=p.left
            r=p.right
            if l:
                res+=str(l.val)+","
                dq.append(l)
            else:
                res+="#"+","
            if r:
                res+=str(r.val)+","
                dq.append(r)
            else:
                res+="#"+","
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="":
            return None
        dq=deque()
        elem=data.split(',')
        r=TreeNode(int(elem[0]))
        dq.append(r)
        i=1
        while dq:
            p=dq.popleft()
            if elem[i]!="#":
                p.left=TreeNode(int(elem[i]))
                dq.append(p.left)
            else:
                p.left=None
            i+=1
            if elem[i]!="#":
                p.right=TreeNode(int(elem[i]))
                dq.append(p.right)
            else:
                p.right=None
            i+=1
        return r
        
