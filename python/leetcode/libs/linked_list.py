class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def to_list(cls, array):
        head = ListNode()

        current_node = head
        for i in array:
            current_node.next = ListNode(i)
            current_node = current_node.next

        return head.next

    def to_array(self):

        curr = self
        result = []
        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
