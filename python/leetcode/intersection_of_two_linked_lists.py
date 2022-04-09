# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        current_a = headA
        current_b = headB

        set_collection = set()

        while current_a or current_b:
            if current_a == current_b:
                return current_a

            if current_a in set_collection:
                return current_a

            if current_b in set_collection:
                return current_b

            if current_a:
                set_collection.add(current_a)
                current_a = current_a.next

            if current_b:
                set_collection.add(current_b)
                current_b = current_b.next

        return None


if __name__ == "__main__":

    # test case
    head_a = ListNode(4)
    head_a.next = ListNode(1)
    head_a.next.next = ListNode(8)
    head_a.next.next.next = ListNode(4)
    head_a.next.next.next.next = ListNode(5)

    head_b = ListNode(5)
    head_b.next = ListNode(6)
    head_b.next.next = ListNode(1)
    head_b.next.next.next = head_a.next.next
    obj = Solution()

    assert obj.getIntersectionNode(head_a, head_b) is head_a.next.next

    # test case
    head_a = ListNode(2)
    head_a.next = ListNode(6)
    head_a.next.next = ListNode(4)

    head_b = ListNode(1)
    head_b.next = ListNode(5)
    obj = Solution()

    assert obj.getIntersectionNode(head_a, head_b) is None

    # test case
    head_a = ListNode(1)
    head_a.next = ListNode(9)
    head_a.next.next = ListNode(1)
    head_a.next.next.next = ListNode(2)
    head_a.next.next.next.next = ListNode(4)

    head_b = ListNode(3)
    head_b.next = head_a.next.next.next
    obj = Solution()

    assert obj.getIntersectionNode(head_a, head_b) is head_a.next.next.next
