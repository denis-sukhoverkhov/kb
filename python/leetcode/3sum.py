from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        result = []
        for i in range(len(nums)):

            if i > 0 and nums[i - 1] == nums[i]:
                continue

            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:
                curr_summ = nums[i] + nums[lp] + nums[rp]

                if curr_summ == 0:
                    el = [nums[i], nums[lp], nums[rp]]
                    if el not in result:
                        result.append(
                            [nums[i], nums[lp], nums[rp]]
                        )

                if curr_summ > 0:
                    rp -= 1
                else:
                    lp += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]

    assert obj.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
