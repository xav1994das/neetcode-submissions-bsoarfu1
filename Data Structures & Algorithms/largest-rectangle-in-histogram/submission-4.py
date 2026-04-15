class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        stack=[]
        #find pse and nse on the fly
        maxarea=0
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                #second codition means - height of i is nse of height at tos
                nseIndex=i #get the i which is the supposedly the nseIndex
                curr=stack[-1] #point for which we are calculating area
                pseIndex=stack[-2] if len(stack)>1 else -1# 
                area=heights[curr]*(nseIndex-pseIndex-1)
                maxarea=max(area,maxarea)
                stack.pop()
            
            stack.append(i)
        
        while stack:
            curr=stack[-1]
            pseIndex=stack[-2] if len(stack)>1 else -1
            nseIndex=n
            area=heights[curr]*(nseIndex-pseIndex-1)
            maxarea=max(area,maxarea)
            stack.pop()
        return maxarea