package main

import "fmt"

type SinglyLinkedListNode struct {
	data int32
	next *SinglyLinkedListNode
}

func printLinkedList(head *SinglyLinkedListNode) {
	node := head
	for node != nil {
		fmt.Println(node.data)
		node = node.next
	}

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

func reversePrint(llist *SinglyLinkedListNode) {
	node := llist
	if node == nil {
		return
	}

	reversePrint(node.next)
	fmt.Println(node.data)

}

func main() {
	llist := SinglyLinkedList{}

	arr := []int32{16, 13, 10, 90}

	for i := 0; i < len(arr); i++ {
		llist.insertNodeIntoSinglyLinkedList(arr[i])
	}

	reversePrint(llist.head)
}
