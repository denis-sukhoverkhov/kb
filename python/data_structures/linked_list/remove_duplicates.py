class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        main_head = head
        prev_node = None

        while head:
            val = head.data
            if not prev_node or val != prev_node.data:
                prev_node = head
                head = head.next
            else:
                prev_node.next = head.next
                head = head.next

        return main_head

    def remove_all_duplicates(self, A):
        curr_head = None

        while A and curr_head is None:
            cur_val = A.data

            f = False
            while A.next and cur_val == A.next.data:
                A = A.next
                f = True
            else:
                if f:
                    A = A.next
                else:
                    curr_head = A
                    break

        if curr_head:
            A = curr_head.next
            last_node = curr_head
            while A:
                cur_val = A.data

                f = False
                while A.next and cur_val == A.next.data:
                    A = A.next
                    f = True
                else:
                    if not f:
                        last_node.next = A
                        last_node = last_node.next
                    else:
                        last_node.next = None
                A = A.next
                # last_node.next.next = None

        return curr_head


if __name__ == "__main__":
    mylist = Solution()
    head = None
    lst = [1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 7, 9]
    for i in range(len(lst)):
        head = mylist.insert(head, lst[i])
    # head = mylist.removeDuplicates(head)
    head = mylist.remove_all_duplicates(head)
    mylist.display(head)
