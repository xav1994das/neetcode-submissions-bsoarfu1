import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #need max heap of size k 
        heap=[]
        for i in range(len(points)):
                d=(points[i][0])**2 + (points[i][1])**2
                heapq.heappush(heap,(-d,points[i]))
        while len(heap)>k:
                heapq.heappop(heap)
        res=[]
        while heap:
                res.append(heapq.heappop(heap)[1])
        return res

        