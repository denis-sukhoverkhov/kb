class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):

        h1 = A
        h2 = B

        new_head = None
        tail = None
        while h1 or h2:

            if h1 and h2:
                if h1.val <= h2.val:
                    new_ll = h1
                    h1 = h1.next
                else:
                    new_ll = h2
                    h2 = h2.next
            elif not h2:
                new_ll = h1
                h1 = h1.next
            elif not h1:
                new_ll = h2
                h2 = h2.next
            else:
                raise Exception("something wrong")

            if new_head is None:
                new_head = new_ll
                tail = new_head
            else:
                tail.next = new_ll
                tail = tail.next

        return new_head


if __name__ == "__main__":
    ll1 = ListNode(5)
    ll1.next = ListNode(8)
    ll1.next.next = ListNode(20)

    ll2 = ListNode(4)
    ll2.next = ListNode(11)
    ll2.next.next = ListNode(15)

    s = Solution()
    s.mergeTwoLists(ll1, ll2)
