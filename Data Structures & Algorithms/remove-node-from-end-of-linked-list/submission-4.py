# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h1=head
        h2=head
        
        for i in range(n):
            h1=h1.next
        if h1 is None:
            return head.next

        while h1.next:
            h1=h1.next
            h2=h2.next
        h2.next=h2.next.next
        return head