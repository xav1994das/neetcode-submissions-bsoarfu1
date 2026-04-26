import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [i for i in stones]
        heapq.heapify_max(heap)
        while heap:
            if len(heap)==1:
                return heap[0]
            p1=heapq.heappop_max(heap)
            p2=heapq.heappop_max(heap)
            if abs(p1-p2)>0:
                heapq.heappush_max(heap,abs(p1-p2))
        return 0
