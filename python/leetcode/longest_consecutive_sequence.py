from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_length = 0
        for i in nums:
            if i - 1 not in nums_set:
                j = i
                while j in nums_set:
                    j += 1
                max_length = max(max_length, j - i)

        return max_length


if __name__ == "__main__":
    obj = Solution()

    nums = [100, 4, 200, 1, 3, 2]
    assert obj.longestConsecutive(nums) == 4

    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    assert obj.longestConsecutive(nums) == 9
