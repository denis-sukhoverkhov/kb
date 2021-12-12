def n_length_combo(lst, n):
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):
        m = lst[i]
        remLst = lst[i + 1 :]

        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)

    return l


class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        lst = [i for i in range(1, A + 1)]

        return n_length_combo(lst, B)


if __name__ == "__main__":
    s = Solution()

    # res = s.combine(4, 2)
    # assert res == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    # res = s.combine(6, 3)
    # assert res == [
    #     [1, 2, 3],
    #     [1, 2, 4],
    #     [1, 2, 5],
    #     [1, 2, 6],
    #     [1, 3, 4],
    #     [1, 3, 5],
    #     [1, 3, 6],
    #     [1, 4, 5],
    #     [1, 4, 6],
    #     [1, 5, 6],
    #     [2, 3, 4],
    #     [2, 3, 5],
    #     [2, 3, 6],
    #     [2, 4, 5],
    #     [2, 4, 6],
    #     [2, 5, 6],
    #     [3, 4, 5],
    #     [3, 4, 6],
    #     [3, 5, 6],
    #     [4, 5, 6]]

    res = s.combine(2, 3)
    assert res == []
