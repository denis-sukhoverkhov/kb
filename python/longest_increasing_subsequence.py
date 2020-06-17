# https://www.interviewbit.com/problems/longest-increasing-subsequence/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        res = [1]*len(A)
        for i in range(1, len(A)):
            for j in range(0, i):
                if A[i] > A[j] and res[i] < res[j] + 1:
                    res[i] = res[j] + 1

        return max(res)


if __name__ == "__main__":
    s = Solution()

    A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert s.lis(A) == 6
