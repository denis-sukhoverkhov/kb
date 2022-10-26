from typing import Optional

from python.leetcode.libs.linked_list import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        prev = None
        while current:

            if prev and prev.val == current.val:
                current = current.next
                prev.next = current
                continue

            prev = current
            current = current.next

        return head


if __name__ == "__main__":
    obj = Solution()

    head = [1, 1, 2]
    head = ListNode.to_list(head)
    obj.deleteDuplicates(head)
    assert head.to_array() == [1, 2]
