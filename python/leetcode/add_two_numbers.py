from typing import Optional

from python.leetcode.libs.linked_list import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = l1
        n2 = l2

        head = None
        current_node = None
        offset = 0
        while n1 is not None or n2 is not None:

            val1 = n1.val if n1 is not None else 0
            val2 = n2.val if n2 is not None else 0
            summ = val1 + val2 + offset
            offset = 0
            if summ > 9:
                offset = 1

            val = summ % 10
            if head is None:
                head = ListNode(val)
                current_node = head
            else:
                current_node.next = ListNode(val)
                current_node = current_node.next

            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        else:
            if offset != 0:
                current_node.next = ListNode(offset)
        return head


if __name__ == "__main__":
    obj = Solution()

    number1 = ListNode(9,
                       ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
    number2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    assert obj.addTwoNumbers(number1, number2).to_array() == [8, 9, 9, 9, 0, 0, 0, 1]

    number1 = ListNode(2, ListNode(4, ListNode(3)))
    number2 = ListNode(5, ListNode(6, ListNode(4)))
    assert obj.addTwoNumbers(number1, number2).to_array() == [7, 0, 8]

    assert obj.addTwoNumbers(ListNode(0), ListNode(0)).val == ListNode(0).val
