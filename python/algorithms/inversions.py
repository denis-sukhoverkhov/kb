class Solution:
    # @param A : list of integers
    # @return an integer
    def countInversions(self, A):
        ct = 0

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    ct += 1

        return ct


if __name__ == "__main__":
    s = Solution()
    A = [2, 4, 1, 3, 5]
    assert s.countInversions(A) == 3
