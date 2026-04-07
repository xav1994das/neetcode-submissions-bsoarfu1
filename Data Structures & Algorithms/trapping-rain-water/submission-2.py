class Solution:
    def trap(self, height: List[int]) -> int:
        prefixMax=[0]*len(height)
        suffixMax=[0]*len(height)
        prefixMax[0]=height[0]
        suffixMax[len(height)-1]=height[len(height)-1]

        for i in range(len(height)-2,0,-1):
            suffixMax[i]=max(suffixMax[i+1], height[i])
        preMax=0
        maxArea=0
        for i in range(len(height)):
            preMax=max(preMax, height[i])
            if (height[i]<preMax and height[i]<suffixMax[i]):
                maxArea += min(preMax, suffixMax[i])-height[i]

        return maxArea