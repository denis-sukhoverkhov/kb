from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        dp = [len(nums) for _ in range(len(nums) - 1)] + [0]
        print(dp)

        for i in range(len(nums) - 2, -1, -1):
            start_idx = i + 1

            subarray = dp[start_idx:start_idx + nums[i]]
            if not subarray:
                dp[i] = len(nums)
            else:
                dp[i] = 1 + min(subarray)

        print(dp)
        return dp[0]


if __name__ == "__main__":
    obj = Solution()

    nums = [2, 3, 1, 1, 4]
    assert obj.jump(nums) == 2
