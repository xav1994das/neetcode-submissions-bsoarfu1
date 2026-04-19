# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        #push all the heads in the pq with their priority
        k=len(lists)
        for i in range(k):
            heapq.heappush(pq,(lists[i].val,i, lists[i]))
        dummy=ListNode(-1)
        p=dummy
        while pq:
            val,k,node=heapq.heappop(pq)
            p.next=node
            p=p.next
            
            if lists[k].next:
                lists[k]=lists[k].next
                heapq.heappush(pq, (lists[k].val,k,lists[k] ))
            
        return dummy.next
