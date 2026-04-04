from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        pos_map=defaultdict(list)
        for i in range(len(strs)):
            word="".join(sorted(strs[i]))
            pos_map[word].append(strs[i])
        
        for ch, val in pos_map.items():
            res.append(val)
        return res

