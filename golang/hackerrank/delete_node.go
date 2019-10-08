package main

import "fmt"

type SinglyLinkedListNode struct {
	data int32
	next *SinglyLinkedListNode
}

type SinglyLinkedList struct {
	head *SinglyLinkedListNode
	tail *SinglyLinkedListNode
}

func (singlyLinkedList *SinglyLinkedList) insertNodeIntoSinglyLinkedList(nodeData int32) {
	node := &SinglyLinkedListNode{
		next: nil,
		data: nodeData,
	}

	if singlyLinkedList.head == nil {
		singlyLinkedList.head = node
	} else {
		singlyLinkedList.tail.next = node
	}

	singlyLinkedList.tail = node
}

func deleteNode(head *SinglyLinkedListNode, position int32) *SinglyLinkedListNode {
	if position == 0 {
		return head.next
	}
	nodeCt := int32(0)
	currNode := head
	prevNode := head
	for nodeCt != position {
		nodeCt++
		prevNode = currNode
		currNode = currNode.next
	}

	prevNode.next = currNode.next

	return head

}

func main() {
	llist := SinglyLinkedList{}

	arr := []int32{7, 11, 12, 8, 18, 16, 5, 18, 0}

	for i := 0; i < len(arr); i++ {
		llist.insertNodeIntoSinglyLinkedList(arr[i])
	}
	fmt.Println(deleteNode(llist.head, 0))
}
