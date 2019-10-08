

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


def compare_lists(llist1, llist2):
    if not llist1 and not llist2:
        return True

    if llist1 and llist2 and llist1.data == llist2.data:
        return compare_lists(llist1.next, llist2.next)

    return False


if __name__ == '__main__':

    llist1 = SinglyLinkedList()

    arr = [1, 2, 3, 4, 5]
    for i in arr:
        llist_head = insertNodeAtHead(llist1.head, i)
        llist1.head = llist_head

    llist2 = SinglyLinkedList()
    arr = [1, 2, 3, 4, 5]
    for i in arr:
        llist_head = insertNodeAtHead(llist2.head, i)
        llist2.head = llist_head

    print(compare_lists(llist1.head, llist2.head))

