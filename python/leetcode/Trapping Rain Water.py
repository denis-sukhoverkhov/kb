from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        l, r = 0, len(height) - 1

        max_l_height = height[0]
        max_r_height = height[-1]
        while l < r:
            if max_l_height <= max_r_height:
                l += 1
                max_l_height = max(max_l_height, height[l])
                res += max_l_height - height[l]
            else:
                r -= 1
                max_r_height = max(max_r_height, height[r])
                res += max_r_height - height[r]

        return res


if __name__ == "__main__":
    obj = Solution()

    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    assert obj.trap(height) == 6
