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

func insertNodeAtPosition(llist *SinglyLinkedListNode, data int32, position int32) *SinglyLinkedListNode {

	nodeCt := int32(0)
	currNode := llist
	prevNode := llist
	for nodeCt != position {
		nodeCt++
		prevNode = currNode
		currNode = currNode.next
	}

	newNode := &SinglyLinkedListNode{
		next: currNode,
		data: data,
	}

	prevNode.next = newNode

	return llist

}

func main() {
	llist := SinglyLinkedList{}

	arr := []int32{16, 13, 7}

	for i := 0; i < len(arr); i++ {
		llist.insertNodeIntoSinglyLinkedList(arr[i])
	}
	fmt.Println(insertNodeAtPosition(llist.head, 1, 2))
}
