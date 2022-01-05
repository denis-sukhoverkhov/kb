from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        p1 = head
        p2 = head.next
        while p2 is not None:
            p1 = p1.next
            if p2.next is None:
                break
            p2 = p2.next.next

        return p1


if __name__ == "__main__":

    obj = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    assert obj.middleNode(head) is head.next.next.next

    head = ListNode(2, ListNode(5, ListNode(9, ListNode(10, ListNode(4)))))
    assert obj.middleNode(head) is head.next.next

