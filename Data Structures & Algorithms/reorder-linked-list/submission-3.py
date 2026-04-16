# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        h1=head
        h2=head
        fe=h1
        while h1.next and h2.next and h2.next.next:
            h1=h1.next
            h2=h2.next.next
            fe=h1        
        cur=fe.next #second pointer head
        pre=None
        nex=None
        while cur:
            nex=cur.next
            cur.next=pre
            pre=cur
            cur=nex
        fe.next=None
        h2=pre #head of the second list in reversed order 
        h1=head
        print("h1")
        while h1 and h2:
            t=h1.next
            x=h2.next
            h1.next=h2
            h2.next=t
            h1=t
            h2=x
        while h1:
            h1=h1.next
        while h2:
            h2=h2.next

        


        
