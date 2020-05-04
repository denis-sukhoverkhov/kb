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


if __name__ == "__main__":
    mylist = Solution()
    head = None
    lst = [1, 1, 2, 3]
    for i in range(4):
        head = mylist.insert(head, lst[i])
    head = mylist.removeDuplicates(head)
    mylist.display(head)
