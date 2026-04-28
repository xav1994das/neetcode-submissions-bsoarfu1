import heapq
class MedianFinder:

    def __init__(self):
        self.s=[]
        self.l=[]

        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.s,num)


        if self.s and self.l and self.s[0]>self.l[0]:
            p=heapq.heappop_max(self.s)
            heapq.heappush(self.l, p)

        if len(self.s)>(len(self.l)+1):
            p=heapq.heappop_max(self.s)
            heapq.heappush(self.l, p)
        if len(self.l)>(len(self.s)+1):
            p=heapq.heappop(self.l)
            heapq.heappush_max(self.s, p)
        
        

    def findMedian(self) -> float:
        if len(self.s)>len(self.l):
            return self.s[0]
        elif len(self.l)>len(self.s):
            return self.l[0]
        else:
            x=self.s[0]
            y=self.l[0]
            print(self.s,self.l)
            return (x+y)/2
        