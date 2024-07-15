from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = nums.copy()
        while n > 1:
            tmp = tmp[:n//2]
            n = len(tmp)

            for i in range(n):

                # even
                if i % 2 == 0:
                    tmp[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    tmp[i] = max(nums[2 * i], nums[2 * i + 1])

            nums = tmp.copy()

        return nums[-1]


if __name__ == "__main__":
    obj = Solution()

    assert obj.minMaxGame(nums=[1, 3, 5, 2, 4, 8, 2, 2]) == 1
    assert obj.minMaxGame(nums=[3]) == 3
