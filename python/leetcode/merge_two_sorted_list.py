# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def to_array(self):
        arr = []
        head = self
        while head is not None:
            arr.append(head.val)
            head = head.next

        return arr


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        current_node = head
        while list1 or list2:

            if list1 is None:
                current_node.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 is None:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                current_node.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                list2 = list2.next

            current_node = current_node.next

        return head.next


if __name__ == "__main__":
    obj = Solution()

    lst1 = None
    lst2 = ListNode(0)
    assert obj.mergeTwoLists(lst1, lst2).to_array() == [0]

    lst1 = ListNode(1, ListNode(2, ListNode(4)))
    lst2 = ListNode(1, ListNode(3, ListNode(4)))
    assert obj.mergeTwoLists(lst1, lst2).to_array() == [1, 1, 2, 3, 4, 4]
