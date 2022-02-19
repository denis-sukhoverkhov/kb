from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def traceback(nums):

            result = []

            if len(nums) == 1:
                return [nums[:]]

            for i in range(len(nums)):
                n = nums.pop(0)
                permutations = traceback(nums)

                for perm in permutations:
                    perm.append(n)

                result.extend(permutations)

                nums.append(n)

            return result

        res = traceback(nums)

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.permute([1, 2]) == [[2, 1], [1, 2]]
    assert obj.permute([1]) == [[1]]

    assert obj.permute([1, 2, 3]) == [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
