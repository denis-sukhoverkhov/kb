from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        ln = len(nums)
        s = []
        res = [0] * ln
        for i in range(ln*2-1, -1, -1):
            idx = i % ln

            while s and s[-1] <= nums[idx]:
                s.pop()

            if not s:
                res[idx] = -1
            else:
                res[idx] = s[-1]

            s.append(nums[idx])

        return res


if __name__ == "__main__":
    obj = Solution()

    nums = [8, 7, 6, 5]
    assert obj.nextGreaterElements(nums) == [-1, 8, 8, 8]

    nums = [1, 2, 1]
    assert obj.nextGreaterElements(nums) == [2, -1, 2]

    nums = [1, 2, 3, 4, 3]
    assert obj.nextGreaterElements(nums) == [2, 3, 4, -1, 4]

