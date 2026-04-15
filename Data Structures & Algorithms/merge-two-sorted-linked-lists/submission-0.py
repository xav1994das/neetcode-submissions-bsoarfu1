# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1=list1
        h2=list2
        h3=ListNode(-1)
        tail=h3
        while h1 and h2:
            if h1.val<=h2.val:
                tail.next=ListNode(h1.val)
                h1=h1.next
            else:
                tail.next=ListNode(h2.val)
                h2=h2.next
            tail=tail.next

        
        while not h2 and h1:
            tail.next=ListNode(h1.val)
            h1=h1.next
            tail=tail.next

        while not h1 and h2:
            tail.next=ListNode(h2.val)
            h2=h2.next
            tail=tail.next
        return h3.next
