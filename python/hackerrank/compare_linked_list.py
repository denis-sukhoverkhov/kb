

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


def mergeLists_rec(head1, head2):

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeLists_rec(head1.next, head2)
    else:
        temp = head2
        temp.next = mergeLists_rec(head1, head2.next)

    return temp

def mergeLists_iter(head1, head2):

    cur_new_list = None

    current1 = head1
    current2 = head2
    new_list_head = None

    while current1 or current2:
        if cur_new_list and not new_list_head:
            new_list_head = cur_new_list

        if not current1:
            cur_new_list.next = current2
            return new_list_head

        if not current2:
            cur_new_list.next = current1
            return new_list_head

        if current1.data <= current2.data:
            cur_new_list = add_node(cur_new_list, current1)
            current1 = current1.next
        else:
            cur_new_list = add_node(cur_new_list, current2)
            current2 = current2.next

    return new_list_head


def add_node(node, new_node):
    if node:
        node.next = new_node
        return node.next
    else:
        node = new_node
        return node


def findMergeNode(head1, head2):
    cur = head1
    while cur is not None:
        cur2 = head2
        while cur2 is not None:
            if cur is cur2:
                return cur.data
            cur2 = cur2.next

        cur = cur.next

    return None


def has_cycle(head):
    slow_p = head
    fast_p = head
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p is fast_p:
            return True

    return False

if __name__ == '__main__':

    llist1 = SinglyLinkedList()

    arr = [3, 2, 1, ]
    for i in arr:
        llist_head = insertNodeAtHead(llist1.head, i)
        llist1.head = llist_head

    llist2 = SinglyLinkedList()
    arr = [4, 3]
    for i in arr:
        llist_head = insertNodeAtHead(llist2.head, i)
        llist2.head = llist_head

    l = mergeLists_iter(llist1.head, llist2.head)
    pass

    print(findMergeNode(llist1.head, llist2.head))

