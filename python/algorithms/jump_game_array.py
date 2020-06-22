class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):

        if not A or A[0] == 0 and len(A) > 1:
            return 0

        if A and A[0] == 0 and len(A) == 1:
            return 1

        jump = 1
        step = A[0]

        max_reach = A[0]

        for i in range(1, len(A)):
            if i == len(A) - 1:
                return 1

            max_reach = max(max_reach, A[i] + i)

            step -= 1

            if step == 0:

                jump += 1

                if i >= max_reach:
                    return 0

                step = max_reach - i

        return 0

    def jump(self, A):

        if not A or A[0] == 0 and len(A) > 1:
            return -1

        if A and A[0] == 0 and len(A) == 1:
            return 0

        res = [0] * len(A)

        for i in range(1, len(A)):
            res[i] = float('inf')
            for j in range(i):
                if i <= j + A[j] and res[j] != float('inf'):
                    res[i] = min(res[i], res[j] + 1)
                    break

        return -1 if res[-1] == 0 else res[-1]


if __name__ == "__main__":
    s = Solution()
    # A = [0]
    #
    # assert s.jump(A) == 0

    A = [0, 46, 46, 0, 2, 47, 1, 24, 45, 0, 0, 24, 18, 29, 27, 11, 0, 0, 40, 12, 4, 0, 0, 0, 49, 42, 13, 5, 12, 45, 10,
         0, 29, 11, 22, 15, 17, 41, 34, 23, 11, 35, 0, 18, 47, 0, 38, 37, 3, 37, 0, 43, 50, 0, 25, 12, 0, 38, 28, 37, 5,
         4, 12, 23, 31, 9, 26, 19, 11, 21, 0, 0, 40, 18, 44, 0, 0, 0, 0, 30, 26, 37, 0, 26, 39, 10, 1, 0, 0, 3, 50, 46,
         1, 38, 38, 7, 6, 38, 27, 7, 25, 30, 0, 0, 36, 37, 6, 39, 40, 32, 41, 12, 3, 44, 44, 39, 2, 26, 40, 36, 35, 21,
         14, 41, 48, 50, 21, 0, 0, 23, 49, 21, 11, 27, 40, 47, 49]

    # assert s.jump(A) ==

    A = [1, 3, 6, 1, 0, 9]

    assert s.jump(A) == 3

    A = [3, 2, 1, 0, 4]

    assert s.jump(A) == float('inf')

    A = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

    assert s.canJump(A) == 1

    A = [2, 3, 1, 1, 4]
    assert s.canJump(A) == 1

    A = [3, 2, 1, 0, 4]
    assert s.canJump(A) == 0
