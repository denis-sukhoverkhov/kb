class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):

        # ma = max(A)

        mapka = {}
        for i in range(len(A)):
            if A[i] in mapka:
                mapka[A[i]].append(A[i] - B)
            else:
                mapka[A[i]] = [
                    A[i] - B,
                ]

        for v in mapka.keys():
            val = mapka[v][0]
            if val in mapka and (val != v or len(mapka[v]) > 1):
                return 1

        return 0


if __name__ == "__main__":
    s = Solution()

    A = [70, 48, 90]
    k = 70
    assert s.diffPossible(A, k) == 0

    A = [1, 5, 4, 1, 2]
    k = 0
    assert s.diffPossible(A, k) == 1

    A = [1, 3, 2]
    k = 0
    assert s.diffPossible(A, k) == 0

    A = [0]
    k = 0
    assert s.diffPossible(A, k) == 0

    A = [1, 5, 3]
    k = 2
    assert s.diffPossible(A, k) == 1
