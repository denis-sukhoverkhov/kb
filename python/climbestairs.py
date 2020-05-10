class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):

        res = [0] * (A + 1)
        res[0], res[1] = 1, 1

        for i in range(2, len(res)):
            res[i] = res[i-1] + res[i-2]

        return res[-1]


if __name__ == "__main__":
    s = Solution()

    A = 5
    assert s.climbStairs(A) == 8
