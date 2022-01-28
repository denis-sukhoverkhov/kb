"""
# Definition for a Node.
"""
from typing import Optional

class Node1:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        _map = {None: None}

        cur = head

        while cur is not None:
            _map[cur] = Node(x=cur.val)
            cur = cur.next

        cur = head
        while cur is not None:
            _map[cur].next = _map[cur.next]
            _map[cur].random = _map[cur.random]
            cur = cur.next

        new_head = _map[head]
        return new_head


if __name__ == "__main__":
    obj = Solution()

    nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]
    # s = hash(Node(7))
    # s1 = hash(Node(8))
    # s2 = hash(Node1(8))
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[2]
    nodes[2].next = nodes[3]
    nodes[3].next = nodes[4]
    nodes[1].random = nodes[0]
    nodes[2].random = nodes[-1]
    nodes[3].random = nodes[2]

    head = nodes[0]
    res = obj.copyRandomList(head)
    pass

