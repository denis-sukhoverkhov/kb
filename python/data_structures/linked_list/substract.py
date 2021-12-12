# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):

        if not A or A.next is None:
            return A

        p, q = A, A
        # ct = 1
        mid = None
        while True:
            p = p.next.next
            if p is None:
                second_start = q.next
                break
            if p.next is None:
                second_start = q.next.next
                mid = q.next
                break

            q = q.next

        q.next = None

        # reverse
        curr = second_start
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        first_start = A
        second_start = prev

        head1 = first_start
        head2 = second_start
        while head1.next and head2.next:
            head1.val = head2.val - head1.val
            head1 = head1.next
            head2 = head2.next
        else:
            head1.val = head2.val - head1.val

        # reverse
        curr = second_start
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        second_start = prev

        if mid:
            head1.next = mid
            mid.next = second_start
        else:
            head1.next = second_start

        return first_start


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    head = ListNode(l[0])
    first = head
    for i in l[1:]:
        head.next = ListNode(i)
        head = head.next

    s = Solution()
    s.subtract(first)
