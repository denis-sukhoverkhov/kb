
class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def rotateRight(self, A, B):

        if not A:
            return A

        tmp = A
        len = 1
        while tmp.next:
            len += 1
            tmp = tmp.next

        if B > len:
            B = B % len

        if B == 0:
            return A

        k = len - B

        if k == 0:
            return A

        cnt = 1
        curr = A
        while cnt < k and curr:
            curr = curr.next
            cnt+=1

        if curr is None:
            return A

        new_head = curr.next

        curr.next = None
        tmp.next = A

        return new_head


if __name__ == "__main__":
    l = [91, 34, 18, 83, 38, 82, 21, 69]
    head = ListNode(l[0])
    first = head
    for i in l[1:]:
        head.next = ListNode(i)
        head = head.next

    s = Solution()
    res = s.rotateRight(first, 90)

    l = [68, 86, 36, 16, 5, 75]
    head = ListNode(l[0])
    first = head
    for i in l[1:]:
        head.next = ListNode(i)
        head = head.next

    s = Solution()
    res = s.rotateRight(first, 90)
    pass

