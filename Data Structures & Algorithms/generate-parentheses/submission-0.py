class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        ds=[]
        def backtrack(openc,closec):
            if openc==n and closec==n:
                res.append("".join(ds))
                return 
            if openc<n:
                ds.append("(")
                backtrack(openc+1, closec)
                ds.pop()
            if closec <openc:
                ds.append(")")
                backtrack(openc, closec+1)
                ds.pop()
        backtrack(0,0)
        return (res)