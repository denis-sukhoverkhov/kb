from collections import defaultdict


class Solution:
    # https://www.interviewbit.com/problems/2-sum/
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):

        s = defaultdict(list)

        res = []
        for i in range(len(A)):
            tmp = B - A[i]
            if tmp in s:
                res.append((s[tmp][0], i+1))
            s[A[i]].append(i+1)

        res = sorted(res, key=lambda i: (i[1], i[0]))

        return list(res[0]) if res else []


if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([ -10, -10, -10 ], -5) == []

    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]

    assert s.twoSum(
        [1, 1, 1, ], 2) == [1, 2]

    assert s.twoSum([ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ], -3) == [4, 8]



