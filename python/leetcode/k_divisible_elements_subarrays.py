from typing import List


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        ln = len(nums)

        sub_set = set()
        for i in range(ln):
            curr_counted_div = 0
            sb = []
            for j in range(i, ln):
                if curr_counted_div == k and nums[j] % p == 0:
                    break

                if nums[j] % p == 0:
                    curr_counted_div += 1

                sb.append(nums[j])
                sub_set.add(tuple(sb))

        return len(sub_set)


if __name__ == "__main__":
    obj = Solution()

    assert obj.countDistinct([10, 2, 17, 7, 20], 1, 10) == 14

    nums = [2, 3, 3, 2, 2]
    k = 2
    p = 2
    assert obj.countDistinct(nums, k, p) == 11
