# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ct=self.worker(head, 0, n)
        if ct==n:
            return head.next
        return head
    def worker(self, head, ct, n):
        if head==None:
            return 0
        ct=self.worker(head.next, ct,n)
        ct+=1
        print(head.val,ct)
        if n+1==ct:
            print(head.val)
            head.next=head.next.next
        return ct
