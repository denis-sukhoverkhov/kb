from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        max_square = 0

        while lp < rp:
            min_height = min(height[lp], height[rp])
            width = rp - lp
            max_square = max(max_square, min_height * width)

            if height[lp] >= height[rp]:
                rp -= 1
            else:
                lp += 1

        return max_square


if __name__ == "__main__":
    obj = Solution()

    assert obj.maxArea([1, 1]) == 1
    assert obj.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
