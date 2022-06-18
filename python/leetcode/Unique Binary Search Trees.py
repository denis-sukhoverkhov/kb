class Solution:
    def numTrees(self, n: int) -> int:

        dp = [1] * (n + 1)

        for number_of_nodes in range(2, n+1):

            total = 0
            for root in range(1, number_of_nodes + 1):
                left = dp[root - 1]
                right = dp[number_of_nodes - root]

                total += left * right

            dp[number_of_nodes] = total

        return dp[n]


if __name__ == "__main__":
    obj = Solution()

    assert obj.numTrees(3) == 5
