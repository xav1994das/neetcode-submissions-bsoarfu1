class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        pos_sp=[]
        st=deque()
        for i in range(n):
            pos_sp.append((position[i],speed[i]))
        pos_sp.sort(key=lambda x: x[0])

        j=n-1
        while j>=0:
            time=(target-pos_sp[j][0])/pos_sp[j][1]
            if st and time<=st[-1]:
                j-=1
                continue
            st.append(time)
            j-=1
        return len(st)