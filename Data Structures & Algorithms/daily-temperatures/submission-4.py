class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        st=deque()
        res=[0]*n
        for i in range(n):
            while st and temperatures[i]>temperatures[st[-1]]:
                idx=st[-1]
                res[idx]=i-idx
                st.pop()
            st.append(i)
        while st:
            p=st.pop()
            res[p]=0
        return res