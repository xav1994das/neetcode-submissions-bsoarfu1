class MinStack:

    def __init__(self):
        self.buffer=[]
        self.arr=[]

    def push(self, val: int) -> None:
        self.arr.append(val)
        l=len(self.buffer)-1
        if l<0:
            self.buffer.append(val)
        else:
            smallest=self.buffer[l]
            if smallest>=val:
                self.buffer.append(val)
            else:
                self.buffer.append(smallest)


    def pop(self) -> None:
        self.arr.pop()
        self.buffer.pop()

    def top(self) -> int:
        l=len(self.arr)-1
        return self.arr[l]

    def getMin(self) -> int:
        l=len(self.buffer)-1
        return self.buffer[l]
