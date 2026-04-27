import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        #min heap of size k
        for x in nums:
            heapq.heappush(heap, x)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
        