from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]

        result = float('-inf')
        for i in range(1, len(nums)):
            res = max_prod * nums[i], min_prod * nums[i], nums[i]
            max_prod = max(*res)
            min_prod = min(*res)

            print(result)

            result = max(result, max_prod)

            # if max_prod == 0:
            #     max_prod = 1
            #     min_prod = 1

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.maxProduct([2, 3, -2, 4]) == 6
