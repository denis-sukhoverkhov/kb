from typing import Optional

from python.leetcode.linked_list_cycle import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False