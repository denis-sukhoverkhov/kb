# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        p1 = head
        p2 = head
        for i in range(n):
            p2 = p2.next

        if p2 is None:
            return p1.next

        next_node = p2.next if p2 else None
        while next_node is not None:
            p1 = p1.next
            p2 = next_node
            next_node = next_node.next

        if p1.next is p2:
            p1.next = None
        else:
            p1.next = p1.next.next

        return head


if __name__ == "__main__":
    obj = Solution()

    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    obj.removeNthFromEnd(head1, 7)
    assert head1.next.val == 2

    head1 = ListNode(1, ListNode(2, ListNode(3)))
    obj.removeNthFromEnd(head1, 1)
    assert head1.next.val == 2

    head1 = ListNode(1, ListNode(2))
    obj.removeNthFromEnd(head1, 2)
    assert head1.next.val == 2

    head1 = ListNode(1, ListNode(2))
    obj.removeNthFromEnd(head1, 1)
    assert head1.next is None

    head2 = ListNode(1)
    result = obj.removeNthFromEnd(head2, 1)
    assert result is None

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    obj.removeNthFromEnd(head, 2)
    assert head.next.next.next.val == 5
