import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while heap:
            if len(heap)==1:
                return -heap[0]
            p1=-heapq.heappop(heap)
            p2=-heapq.heappop(heap)
            if p1!=p2:
                heapq.heappush(heap,-(p1 - p2))
        return 0
