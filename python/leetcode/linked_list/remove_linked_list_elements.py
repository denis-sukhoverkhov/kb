from typing import Optional

from python.leetcode.libs.linked_list import ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy_head = ListNode(next=head)

        current_node = dummy_head
        while current_node and current_node.next:
            if current_node.next.val == val:
                next_node = current_node.next
                if next_node.next:
                    current_node.next = next_node.next
                else:
                    current_node.next = None
            else:
                current_node = current_node.next

        return dummy_head.next


if __name__ == "__main__":
    obj = Solution()

    head = [7, 7, 7, 7]
    head = ListNode.to_list(head)
    val = 7
    assert obj.removeElements(head, val) is None

    head = [1, 2, 6, 3, 4, 5, 6]
    head = ListNode.to_list(head)
    val = 6
    res = obj.removeElements(head, val)
    assert res.to_array() == [1, 2, 3, 4, 5]
