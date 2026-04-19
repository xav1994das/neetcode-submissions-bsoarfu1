# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, t):
        pre=None
        nex=None
        curr=t
        while curr:
            nex=curr.next
            curr.next=pre
            pre=curr
            curr=nex
        return pre
            

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prev=head
        t=temp
        i=1
        if k==1:
            return head
        while True:
            while t and t.next and i<k:
                t=t.next
                i+=1
                node_k=t
            if i<k: #value of i should always be equal to k, if it's not, then there is no k group
                prev.next=temp
                break
            newListHead=t.next
            node_k.next=None
            reversedHead=self.reverse(temp)
            if head==temp:
                head=reversedHead
            else:
                prev.next=reversedHead
            prev=temp
            temp=newListHead
            t=temp
            i=1
        return head
        
