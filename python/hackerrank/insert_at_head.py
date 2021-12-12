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


def insertNodeAtHead(llist, data):
    if llist is None:
        return SinglyLinkedListNode(node_data=data)

    node = SinglyLinkedListNode(node_data=data)
    node.next = llist

    return node


if __name__ == "__main__":

    llist = SinglyLinkedList()

    arr = [1, 2, 3, 4, 5]
    for i in arr:
        llist_head = insertNodeAtHead(llist.head, i)
        llist.head = llist_head
