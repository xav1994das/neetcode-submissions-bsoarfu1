class KthLargest:

    def parent(self,index):
        return (index-1)//2
    def left(self,index):
        return  2*index+1
    def right(self,index):
        return 2*index+2
    def addtoheap(self,node):
        self.heap.append(node)
        self.heap_up(len(self.heap)-1)

    def removefromHeap(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_down(0)

        return root

    def heap_up(self, index):
        while index>0 and self.heap[index]<self.heap[self.parent(index)]:
            parent_index=self.parent(index)
            self.heap[index],self.heap[self.parent(index)]=self.heap[self.parent(index)],self.heap[index]
            index=parent_index

    def heap_down(self,index):
        size=len(self.heap)
        
        while True:
            smallest=index
            l=self.left(index)
            r=self.right(index)
            if l<size and self.heap[l]<self.heap[smallest]:
                smallest=l
            if r<size and self.heap[r]<self.heap[smallest]:
                smallest=r
            if smallest==index:
                break
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            index=smallest
        



    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.k=k
        for i in range(len(nums)):
            self.addtoheap(nums[i])
        



    def add(self, val: int) -> int:
        self.addtoheap(val)
        while len(self.heap)>self.k:
            self.removefromHeap()
        return self.heap[0]
        
