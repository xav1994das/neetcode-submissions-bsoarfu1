class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        pos_map={}
        for i in range(len(strs)):
            word="".join(sorted(strs[i]))

            if word not in pos_map:
                pos_map[word]=[]
            pos_map[word].append(strs[i])
        
        for ch, val in pos_map.items():
            res.append(val)
        return res

