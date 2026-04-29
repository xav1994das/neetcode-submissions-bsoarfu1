class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        res=""
        def backtrack(index,r,c):
            if index==len(word):
                return True
            

            if 0<=r<rows and 0<=c<cols:
                if (board[r][c]!=word[index] or board[r][c]=="#"):
                    return False
                temp=board[r][c]
                board[r][c]="#"
                print(res, word[index], index,r,c)
                l1=backtrack(index+1,r, c+1)
                l2=backtrack(index+1,r, c-1)
                l3=backtrack(index+1,r-1, c)
                l4=backtrack(index+1,r+1, c)
                board[r][c]=temp
                return l1 or l2 or l3 or l4
                
            return False
        for i in range(rows):
            for j in range(cols):
                if backtrack(0,i,j)==True:
                    return True
                    
        return False
        
        