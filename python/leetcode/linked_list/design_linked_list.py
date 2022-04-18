class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.root = Node()
        self.tail = self.root

    def get(self, index: int) -> int:

        current_idx = index
        current_node = self.root.next
        while current_idx > 0 and current_node:
            current_node = current_node.next
            current_idx -= 1

        return current_node.val if current_node else -1

    def addAtHead(self, val: int) -> None:
        self.root.next = Node(val=val, next=self.root.next)

    def addAtTail(self, val: int) -> None:

        curr = self.root

        while curr.next:
            curr = curr.next

        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:

        current_idx = index
        current_node = self.root
        while current_idx > 0 and current_node:
            current_node = current_node.next
            current_idx -= 1

        if current_node:
            current_node.next = Node(val, next=current_node.next)

    def deleteAtIndex(self, index: int) -> None:
        current_idx = index
        current_node = self.root
        while current_idx > 0 and current_node:
            current_node = current_node.next
            current_idx -= 1

        if current_node:
            current_node.next = current_node.next.next if current_node.next else None


if __name__ == "__main__":
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(3, 2)
    # assert myLinkedList.get(1) == 2
    # myLinkedList.deleteAtIndex(1)
    # assert myLinkedList.get(1) == 3
    # assert myLinkedList.get(3) == -1
    # myLinkedList.deleteAtIndex(3)

    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)
    assert myLinkedList.get(1) == 2
    myLinkedList.deleteAtIndex(1)
    assert myLinkedList.get(1) == 3
    assert myLinkedList.get(3) == -1
    myLinkedList.deleteAtIndex(3)

    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(4)
    assert myLinkedList.get(1) == -1

    myLinkedList = MyLinkedList()
    myLinkedList.addAtTail(1)
    assert myLinkedList.get(0) == 1
    myLinkedList.addAtTail(2)
    assert myLinkedList.get(1) == 2
    myLinkedList.deleteAtIndex(1)
    assert myLinkedList.get(0) == 1


    myLinkedList = MyLinkedList()
    myLinkedList.addAtTail(1)
    assert myLinkedList.get(0) == 1
    myLinkedList.addAtTail(2)
    assert myLinkedList.get(1) == 2
    myLinkedList.deleteAtIndex(1)
    assert myLinkedList.get(0) == 1

    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.deleteAtIndex(0)

    myLinkedList = MyLinkedList()
    myLinkedList.addAtIndex(0, 10)
    myLinkedList.addAtIndex(0, 20)
    myLinkedList.addAtIndex(1, 30)
    assert myLinkedList.get(0) == 20

    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)
    assert myLinkedList.get(1) == 2
    myLinkedList.deleteAtIndex(0)
    assert myLinkedList.get(0) == 2

    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(1)
    myLinkedList.addAtTail(3)
    myLinkedList.addAtIndex(1, 2)
    assert myLinkedList.get(1) == 2
    myLinkedList.deleteAtIndex(1)
    assert myLinkedList.get(1) == 3
