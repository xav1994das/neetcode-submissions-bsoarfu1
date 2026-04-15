class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        pse=[-1]*n
        nse=[-1]*n
        stack=[]
        for i in range(0,n):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            pse[i]=stack[-1] if stack else -1
            stack.append(i)
        stack=[]
        print("pse" , pse)
        for i in range(n-1,-1,-1):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            nse[i]= stack[-1] if stack else -1
            stack.append(i)
        stack=[]

        print("nse",nse)
        print("pse", pse)

        maxArea=-1
        area=0
        for i in range(0, n):
            if nse[i]<0:
                nse[i]=n
            if pse[i]<0:
                pse[i]=-1
            width=nse[i]-pse[i]-1
            print(width)
            area=heights[i]*(nse[i]-pse[i]-1)
            maxArea=max(area,maxArea)
        return maxArea

        