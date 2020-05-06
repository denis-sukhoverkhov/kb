# https://www.interviewbit.com/problems/combination-sum-ii/

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

        res = comb_sum(A, B)
        return res


if __name__ == "__main__":
    s = Solution()

    A = [15, 8, 15, 10, 19, 18, 10, 3, 11, 7, 17]
    res = s.combinationSum(A, 33)
    assert res == [[3, 7, 8, 15], [3, 11, 19], [3, 15, 15], [7, 8, 18], [7, 11, 15], [8, 10, 15], [15, 18]]

    A = [7, 1, 3, 5]
    res = s.combinationSum(A, 8)
    assert res == [[1, 7], [3, 5]]

    A = [7, 1]
    res = s.combinationSum(A, 8)
    assert res == [[1, 7]]

    A = []
    res = s.combinationSum(A, 8)
    assert res == []

    A = [8]
    res = s.combinationSum(A, 8)
    assert res == [[8]]
