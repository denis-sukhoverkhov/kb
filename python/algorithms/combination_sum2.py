def comb_sum(lst, n):
    if n < 0:
        return [[]]

    res = []
    for i in range(len(lst)):
        cur_val = lst[i]
        rem = lst[i + 1:]
        if cur_val == n:
            res.append([cur_val])
            return res

        for p in comb_sum(rem, n - cur_val):
            arr = [cur_val] + p
            if sum(arr) == n and arr not in res:
                res.append(arr)

    return res


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()

        new_arr = []
        tmp = [[i] * (B // i) for i in A]
        for i in tmp:
            new_arr += i

        res = comb_sum(new_arr, B)
        return res


if __name__ == "__main__":
    s = Solution()

    A = [8, 10, 6, 11, 1, 16, 8]
    res = s.combinationSum(A, 28)
    assert res == [[2, 2, 3], [7]]

    A = [2, 3, 6, 7]
    res = s.combinationSum(A, 7)
    assert res == [[2, 2, 3], [7]]
