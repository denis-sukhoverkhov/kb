from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        size = len(nums)
        last_idx = size - 1

        dp = {
            last_idx: (1, None)
        }

        for i in range(size - 2, -1, -1):

            tmp_len = 0
            tmp_sign = None
            for j in range(i + 1, size):
                diff = nums[i] - nums[j]
                sign = dp[j][1]

                if diff == 0 or sign is not None and ((diff < 0 and sign < 0) or (diff > 0 and sign > 0)):
                    continue

                if tmp_len < dp[j][0]:
                    tmp_len = dp[j][0]
                    tmp_sign = -1 if diff < 0 else 1

            dp[i] = (1 + tmp_len, tmp_sign)

        return dp[0][0]


if __name__ == "__main__":
    obj = Solution()

    assert obj.wiggleMaxLength([0, 0]) == 1
    assert obj.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert obj.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6

