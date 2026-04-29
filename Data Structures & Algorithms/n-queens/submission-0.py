class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        #imagine our placement looks [0,2]
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
                if canPlace(row,col,placement):
                    placement.append(row)
                    func(col+1, placement)
                    placement.pop()
                
        func(0,[])
        return (res)