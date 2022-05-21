from typing import Optional
from python.leetcode.libs.linked_list import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        root = head
        current_head = ListNode()
        current_head.next = root
        while root and root.next:
            next_node = root.next
            root.next = next_node.next
            next_node.next = current_head.next
            current_head.next = next_node

        return current_head.next


if __name__ == "__main__":
    obj = Solution()

    head = [1, 2, 3, 4, 5]
    head = ListNode.to_list(head)
    res = obj.reverseList(head)
    assert res.to_array() == [5, 4, 3, 2, 1]

    head = [1, 2]
    head = ListNode.to_list(head)
    res = obj.reverseList(head)
    assert res.to_array() == [2, 1]

    head = []
    head = ListNode.to_list(head)
    assert obj.reverseList(head) is None
