import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        heap=[]
        dq=deque()
        char_map=collections.defaultdict(int)
        char_map=collections.Counter(tasks)
        for k,v in char_map.items():
            heapq.heappush_max(heap, v)
        while heap or dq:
            time+=1
            if dq and time==dq[0][1]:
                heapq.heappush_max(heap,dq.popleft()[0])
            x=heapq.heappop_max(heap) if heap else "idle"
            if x!="idle":
                if x-1!=0:
                    dq.append((x-1,time+n+1))
        return time
