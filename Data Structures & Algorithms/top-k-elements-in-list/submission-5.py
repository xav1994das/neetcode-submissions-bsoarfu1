from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        res=[]
        for i in range(len(nums)):
            count[nums[i]] += 1
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        print(sorted_items)
        for i in range(k):
            res.append(sorted_items[i][0])
        return res
