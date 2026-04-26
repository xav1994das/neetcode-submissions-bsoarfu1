import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #need max heap of size k 
        heap=[]
        for i in range(len(points)):
                d=math.sqrt((points[i][0])**2 + (points[i][1])**2)
                heapq.heappush(heap,(-d,points[i]))
                if len(heap)>k:
                        heapq.heappop(heap)

        #while len(heap)>k:
                
        res=[]
        while heap:
                res.append(heapq.heappop(heap)[1])
        return res

        