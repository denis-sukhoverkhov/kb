from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx = float('-inf')
        for i in accounts:
            mx = max(mx, sum(i))

        return mx


if __name__ == "__main__":
    obj = Solution()

    accounts = [[1, 2, 3], [3, 2, 1]]
    assert obj.maximumWealth(accounts) == 6
