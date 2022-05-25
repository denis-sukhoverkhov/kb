from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        stack = []

        min_val = nums[0]
        for i in nums[1:]:
            while stack and stack[-1][0] < i:
                stack.pop()

            min_val = min(min_val, i)
            stack.append((i, min_val))

            if len(stack) >=2:
                k = stack[-1][0]
                j = stack[-2][0]
                i = stack[-2][1]

                if i < k < j:
                    return True

        return False


if __name__ == "__main__":
    obj = Solution()

    nums = [3, 5, 0, 3, 4]
    assert obj.find132pattern(nums) is True

    nums = [-1, 3, 2, 0]
    assert obj.find132pattern(nums) is True

    nums = [3, 1, 4, 2]
    assert obj.find132pattern(nums) is True

    nums = [1, 2, 3, 4]
    assert obj.find132pattern(nums) is False
