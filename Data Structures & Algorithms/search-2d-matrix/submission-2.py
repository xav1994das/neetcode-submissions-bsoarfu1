class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=len(matrix)-1
        row=-1
        while i<=j:
            m=(i+j)//2
            cols=len(matrix[m])
            if target>=matrix[m][0] and target<=matrix[m][cols-1]:
                row=m
                break
            if target<matrix[m][0]:
                j=m-1
            else:
                i=m+1
        if row==-1:
            return False
        l=0
        h=len(matrix[row])-1
        print(type(l),type(h))
        while l<=h:
            m=(l+h)//2
            if matrix[row][m]==target:
                return True
            elif matrix[row][m]<target:
                l=m+1
            else:
                h=m-1
        
        return False