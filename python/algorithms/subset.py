import copy


def subsetsUtil(A, subset, idx, res):
    for i in range(idx, len(A)):
        subset.append(A[i])

        res.append(copy.copy(subset))
        subsetsUtil(A, subset, i+1, res)

        subset.pop(-1)


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):

        idx = 0
        subset = []
        res = [
            [],
        ]

        A.sort()
        subsetsUtil(A, subset, idx, res)

        return res


if __name__ == "__main__":
    s = Solution()

    A = [1, 2, 3]
    assert s.subsets(A) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
