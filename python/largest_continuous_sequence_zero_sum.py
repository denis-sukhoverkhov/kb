class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        hm = {}

        sum = 0
        res = []
        for i in range(len(A)):
            sum += A[i]

            if sum == 0:
                res.append(A[:i + 1])

            if sum in hm:
                res.append(A[hm[sum] + 1:i + 1])
            else:
                hm[sum] = i

        new_res = sorted(res, key=lambda i: len(i), reverse=True)

        return new_res[0] if new_res else []


if __name__ == "__main__":
    s = Solution()

    A = [0]
    assert s.lszero(A) == [0]

    A = [1, 2, -3, 3]
    assert s.lszero(A) == [1, 2, -3]

    A = [1, 2, -2, 4, -4]
    assert s.lszero(A) == [2, -2, 4, -4]
