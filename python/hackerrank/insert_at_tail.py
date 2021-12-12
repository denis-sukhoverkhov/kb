class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtTail(head, data):

    if head is None:
        return SinglyLinkedListNode(node_data=data)

    node = head
    while node.next is not None:
        node = node.next

    node.next = SinglyLinkedListNode(node_data=data)

    return head


if __name__ == "__main__":

    llist = SinglyLinkedList()

    arr = [1, 2, 3, 4, 5]
    for i in arr:
        llist_head = insertNodeAtTail(llist.head, i)
        llist.head = llist_head
