# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        h1=head
        h2=head

        while h1.next and h2.next and h2.next.next:
            h1=h1.next
            h2=h2.next.next
            if h1==h2:
                return True
        return False