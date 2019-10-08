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

func reversePrint(llist *SinglyLinkedListNode) {
	node := llist
	if node == nil {
		return
	}

	reversePrint(node.next)
	fmt.Println(node.data)

}

func printLinkedList(head *SinglyLinkedListNode) {
	node := head
	for node != nil {
		fmt.Println(node.data)
		node = node.next
	}

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
	fmt.Println(insertNodeAtPosition(llist.head, 1, 2))

	fmt.Println(deleteNode(llist.head, 0))

	reversePrint(llist.head)

	printLinkedList(llist.head)

	fmt.Println(reverse(llist.head))
}
