from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        ln = len(nums)

        curr_subset = []
        def backtrack(idx):
            if idx >= ln:
                result.append(curr_subset.copy())
                return

            curr_subset.append(nums[idx])
            backtrack(idx+1)

            curr_subset.pop()
            backtrack(idx + 1)

        backtrack((0))

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.subsets([9, 0, 3, 5, 7]) == [[9, 0, 3, 5, 7], [9, 0, 3, 5], [9, 0, 3, 7], [9, 0, 3], [9, 0, 5, 7], [9, 0, 5], [9, 0, 7], [9, 0], [9, 3, 5, 7], [9, 3, 5], [9, 3, 7], [9, 3], [9, 5, 7], [9, 5], [9, 7], [9], [0, 3, 5, 7], [0, 3, 5], [0, 3, 7], [0, 3], [0, 5, 7], [0, 5], [0, 7], [0], [3, 5, 7], [3, 5], [3, 7], [3], [5, 7], [5], [7], []]

    assert obj.subsets([1, 2, 3]) == [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
