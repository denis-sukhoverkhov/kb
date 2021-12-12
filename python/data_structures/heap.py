import copy
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        # first_elements_for_heap = [i for i in A]

        new_ll = None
        new_head = None
        while A:
            self.build_heap(A)
            # min = A[0]
            least = A[0].next
            if new_ll is None:
                new_ll = copy.copy(A[0])
                new_ll.next = None
                new_head = new_ll
            else:
                new_ll.next = copy.copy(A[0])
                new_ll = new_ll.next
                new_ll.next = None

            if least:
                A[0] = least
            else:
                A.pop(0)

        return new_head

    @classmethod
    def heapify(cls, arr: List[ListNode], idx_node):
        l = 2 * idx_node + 1
        r = 2 * idx_node + 2

        l_a = len(arr)
        idx_of_min_elem = idx_node
        if l < l_a and arr[l].val < arr[idx_of_min_elem].val:
            idx_of_min_elem = l

        if r < l_a and arr[r].val < arr[idx_of_min_elem].val:
            idx_of_min_elem = r

        if idx_of_min_elem != idx_node:
            arr[idx_node], arr[idx_of_min_elem] = arr[idx_of_min_elem], arr[idx_node]

            cls.heapify(arr, idx_of_min_elem)

    @classmethod
    def build_heap(cls, arr):
        mid = int(len(arr) / 2) - 1
        for i in range(mid, -1, -1):
            cls.heapify(arr, i)

    @classmethod
    def print(cls, new_head: ListNode):
        cur = new_head
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next

        return res


if __name__ == "__main__":
    s = Solution()

    # arrays = [
    #     [5, 7, 9, 10],
    #     [0, 11, 12, 13, 15],
    #     [1, 3, 5, 6, 7, 7, 7, 29],
    # ]
    #
    # ll = []
    # for i in range(len(arrays)):
    #     row = arrays[i]
    #
    #     tmp = None
    #     head = None
    #     for j in range(len(row)):
    #         if tmp is None:
    #             tmp = ListNode(row[j])
    #             head = tmp
    #         else:
    #             tmp.next = ListNode(row[j])
    #             tmp = tmp.next
    #     ll.append(head)
    #
    # ll_res = s.mergeKLists(ll)
    # assert s.print(ll_res) == [0, 1, 3, 5, 5, 6, 7, 7, 7, 7, 9, 10, 11, 12, 13, 15, 29]

    arrays = [
        [8, 20, 38, 44, 55, 65, 66, 79, 87],
        [
            68,
            72,
        ],
        [
            5,
            55,
            61,
            73,
            89,
        ],
        [
            30,
            73,
        ],
        [
            28,
            73,
            84,
            96,
        ],
        [
            54,
            82,
            83,
        ],
        [
            15,
            33,
            38,
            94,
            100,
        ],
        [
            4,
        ],
        [
            22,
            32,
            42,
            64,
            86,
        ],
        [11, 78],
    ]

    ll = []
    for i in range(len(arrays)):
        row = arrays[i]

        tmp = None
        head = None
        for j in range(len(row)):
            if tmp is None:
                tmp = ListNode(row[j])
                head = tmp
            else:
                tmp.next = ListNode(row[j])
                tmp = tmp.next
        ll.append(head)

    ll_res = s.mergeKLists(ll)
    pp = s.print(ll_res)
    assert pp == [
        4,
        5,
        8,
        11,
        15,
        20,
        22,
        28,
        30,
        32,
        33,
        38,
        38,
        42,
        44,
        54,
        55,
        55,
        61,
        64,
        65,
        66,
        68,
        72,
        73,
        73,
        73,
        78,
        79,
        82,
        83,
        84,
        86,
        87,
        89,
        94,
        96,
        100,
    ]
