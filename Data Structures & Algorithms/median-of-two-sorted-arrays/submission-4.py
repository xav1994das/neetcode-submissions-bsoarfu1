class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1
        n=len(nums1)+len(nums2)
        n1=len(nums1)
        n2=len(nums2)
        low=0
        high=len(nums1)
        left=(n+1)//2
        print(left)
        while low<=high:
            mid1=(low+high)//2
            mid2=left-mid1

            l1=nums1[mid1-1] if mid1-1>=0 else float('-inf')
            l2=nums2[mid2-1] if mid2-1>=0 else float('-inf')
            r1=nums1[mid1] if mid1<n1 else float('inf')
            r2=nums2[mid2] if mid2<n2 else float('inf')

            if l1<=r2 and l2<=r1:
                #median found
                if n%2==0:
                    return (max(l1,l2)+min(r1,r2))/2.0
                else:
                    return max(l1,l2)
            elif l1>r2:
                high=mid1-1
            elif l2>r1:
                low=mid1+1
            
