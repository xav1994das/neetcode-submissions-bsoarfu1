"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        l2={} 
        h1=head
        dummy=Node(-1)
        p=dummy
        while h1:
            p.next=Node(h1.val,None,None)
            l2[h1]=p.next
            h1=h1.next
            p=p.next
        t=dummy.next
        h1=head
        while h1:
            o_rand=h1.random
            if o_rand is None:
                t.random = None
            else:
                t.random=l2[o_rand]
            t=t.next
            h1=h1.next

        return dummy.next