from typing import Optional


# Definition for singly-linked list.
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        mid_node = self.get_mid_node(head)

        left_ll = head
        right_ll = mid_node.next
        mid_node.next = None

        left_sorted_ll = self.sortList(left_ll)
        right_sorted_ll = self.sortList(right_ll)

        left_node = left_sorted_ll
        right_node = right_sorted_ll

        dummy_head = ListNode()
        current_node = dummy_head
        while left_node or right_node:
            if not left_node:
                current_node.next = right_node
                right_node = right_node.next
            elif not right_node:
                current_node.next = left_node
                left_node = left_node.next
            elif right_node.val < left_node.val:
                current_node.next = right_node
                right_node = right_node.next
            else:
                current_node.next = left_node
                left_node = left_node.next

            current_node = current_node.next

        return dummy_head.next

    def get_mid_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    obj = Solution()

    head = ListNode(4, next=ListNode(2, next=ListNode(1, next=ListNode(3))))
    assert obj.sortList(head).to_array() == [1, 2, 3, 4]

    head = None
    assert obj.sortList(head) is None

    head = ListNode(4, next=ListNode(1))
    assert obj.sortList(head).to_array() == [1, 4]

    head = ListNode(4)
    assert obj.sortList(head).to_array() == [4]
