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

func reverse(head *SinglyLinkedListNode) *SinglyLinkedListNode {

	curNode := head
	var prev *SinglyLinkedListNode
	for curNode != nil {
		next := curNode.next
		curNode.next = prev
		prev = curNode
		curNode = next
	}

	return prev
}

func main() {
	llist := SinglyLinkedList{}

	arr := []int32{16, 13, 7}

	for i := 0; i < len(arr); i++ {
		llist.insertNodeIntoSinglyLinkedList(arr[i])
	}
	fmt.Println(reverse(llist.head))
}
