from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        max_len = 0

        negative_positions = []
        negative_numbers = 0
        start_pos = 0
        for i in range(len(nums)):
            val = nums[i]

            if val < 0:
                negative_numbers += 1
                if not negative_positions:
                    negative_positions.append(i)
                    negative_positions.append(None)
                else:
                    negative_positions[-1] = i

            if val == 0:
                max_len = max(max_len, self.get_current_len(start_pos, i - 1, negative_numbers,
                                                            negative_positions))

                negative_positions = []
                negative_numbers = 0
                start_pos = i + 1

        if start_pos < len(nums):
            max_len = max(max_len, self.get_current_len(start_pos, len(nums) - 1, negative_numbers,
                                                        negative_positions))

        return max_len

    def get_current_len(self, start, end, negative_numbers, negative_positions):
        full_len = end - start + 1
        if negative_numbers % 2 == 0 or not negative_numbers:
            return full_len

        prefix_len = negative_positions[0] - start + 1
        negative_position_end = negative_positions[1] or negative_positions[0]
        suffix_len = end - negative_position_end + 1
        return full_len - min(prefix_len, suffix_len)


if __name__ == "__main__":
    obj = Solution()

    assert obj.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]) == 4
