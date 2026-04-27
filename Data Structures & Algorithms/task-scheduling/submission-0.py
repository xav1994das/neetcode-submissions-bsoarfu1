import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time=0
        heap=[]
        dq=deque()
        char_map=collections.defaultdict(int)
        for i in tasks:
            char_map[i]+=1
        for k,v in char_map.items():
            heapq.heappush_max(heap, v)
        while heap or dq:
            time+=1
            if dq and time==dq[0][1]:
                q=dq.popleft()
                heapq.heappush_max(heap,q[0])
            x=heapq.heappop_max(heap) if heap else "idle"
            
            if x!="idle":
                if x-1!=0:
                    dq.append((x-1,time+n+1))
            print(dq)
        return time
