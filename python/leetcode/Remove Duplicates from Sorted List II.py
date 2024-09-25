from typing import Optional

from python.leetcode.libs.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new_head = ListNode()
        tail = new_head
        prev_val = None
        current = head

        while current:
            if current.val != prev_val and (not current.next or current.next.val != current.val):
                tail.next = current
                current = current.next
                tail = tail.next
                tail.next = None
                continue

            prev_val = current.val
            current = current.next

        return new_head.next


if __name__ == "__main__":
    obj = Solution()

    root = ListNode.to_list([1, 2, 2])
    new_list = obj.deleteDuplicates(root)
    assert new_list.to_array() == [1]

    root = ListNode.to_list([1, 1])
    new_list = obj.deleteDuplicates(root)
    assert new_list is None

    root = ListNode.to_list([1, 2, 3, 3, 4, 4, 5])
    new_list = obj.deleteDuplicates(root)
    assert new_list.to_array() == [1, 2, 5]
