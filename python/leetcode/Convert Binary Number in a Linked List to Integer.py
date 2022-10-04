from python.leetcode.add_two_numbers import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        res = head.val
        curr = head.next

        while curr:
            res = (res << 1) | curr.val
            # res <<= curr.val
            curr = curr.next

        return res


if __name__ == "__main__":
    obj = Solution()

    head = ListNode.to_list([1, 0, 1])
    assert obj.getDecimalValue(head) == 5
