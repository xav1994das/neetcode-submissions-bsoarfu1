class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        pos_sp_map=collections.defaultdict(int)
        st=deque()
        for i in range(n):
            pos_sp_map[position[i]]=speed[i]
        pos_sp_map={k:v for k,v in sorted(pos_sp_map.items(), key=lambda x:x[0], reverse=True)}

        
        for k,v in pos_sp_map.items():
            time=(target-k)/v
            if st and time<=st[-1]:
                continue
            st.append(time)
        return len(st)