class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def getKth(self, curr, k):
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr

    def reverseKGroup(self, head, k):
        if k == 1 or not head:
            return head

        temp = head
        prev = None

        while temp:
            kth = self.getKth(temp, k)

            # ❗ If kth node doesn't exist → stop
            if not kth:
                if prev:
                    prev.next = temp
                break

            nextGroup = kth.next
            kth.next = None  # cut

            reversedHead = self.reverse(temp)

            if not prev:
                head = reversedHead
            else:
                prev.next = reversedHead

            # temp is now the tail after reversal
            prev = temp
            temp = nextGroup

        return head