class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        #imagine our placement looks [0,2]
        upperDiagonal=[0]*(2*n-1)
        lowerDiagonal=[0]*(2*n-1)
        leftRow=[0]*n
        def canPlace(r,c,place):
            if r in place:
                return False
            for i in range(len(place)):
                if abs(r-place[i])==abs(c-i):
                    return False
            return True

        def func(col,placement):
            if col==n:
                strs=[]
                for i in placement:
                    p=""
                    for j in range(n):
                        p+="." if  j!=i else "Q"
                    strs.append(p)
                res.append(strs)
                return
            for row in range(n):
                #place Q in position row, col, check if it can happen
                #if canPlace(row,col,placement):
                if (leftRow[row]==0 and lowerDiagonal[row+col]==0 and
                upperDiagonal[n-1+col-row]==0):
                    placement.append(row)
                    leftRow[row]=1
                    lowerDiagonal[row+col]=1
                    upperDiagonal[n-1+col-row]=1
                    func(col+1, placement)
                    placement.pop()
                    upperDiagonal[n-1+col-row]=0
                    lowerDiagonal[row+col]=0
                    leftRow[row]=0
                
        func(0,[])
        return (res)