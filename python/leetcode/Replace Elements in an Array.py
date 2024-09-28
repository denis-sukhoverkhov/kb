from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        st = {nums[i]: i for i in range(len(nums))}
        for op in operations:
            idx = st[op[0]]
            st[op[1]] = idx
            del st[op[0]]

        st = {v: k for k, v in st.items()}
        lst = sorted(st.items())

        return [i[1] for i in lst]


if __name__ == "__main__":
    obj = Solution()

    nums = [1, 2]
    operations = [[1, 3], [2, 1], [3, 2]]
    assert obj.arrayChange(nums, operations) == [2, 1]

    nums = [1, 2, 4, 6]
    operations = [[1, 3], [4, 7], [6, 1]]
    assert obj.arrayChange(nums, operations) == [3, 2, 7, 1]
