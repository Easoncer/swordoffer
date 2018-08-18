# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        s, s.next = ListNode(0), head
        p , q = s, s

        while p :
            if n == 0:
                break
            n -= 1
            p = p.next

        if n >= 1 :
            return None

        while p.next:
            q = q.next
            p = p.next
        q.next = q.next.next
        return s.next