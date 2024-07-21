from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        min_average_val = float('inf')
        min_average_idx = None

        sum_first_part = 0
        len_first_part = 0

        sum_second_part = sum(nums)
        len_second_part = len(nums)
        n = len(nums)
        for i in range(n):
            len_first_part += 1
            sum_first_part += nums[i]
            avg_first_part = int(sum_first_part / len_first_part)

            len_second_part -= 1
            if len_second_part == 0:
                avg_second_part = 0
            else:
                sum_second_part -= nums[i]
                avg_second_part = int(sum_second_part / len_second_part)

            diff = abs(avg_first_part - avg_second_part)
            if diff < min_average_val:
                min_average_val = diff
                min_average_idx = i

        return min_average_idx


if __name__ == "__main__":
    obj = Solution()

    nums = [0]
    assert obj.minimumAverageDifference(nums) == 0

    nums = [2, 5, 3, 9, 5, 3]
    assert obj.minimumAverageDifference(nums) == 3