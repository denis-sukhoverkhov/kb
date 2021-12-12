import random


def generate_random_sorted_list(size=100, start=1, end=1000):
    tmp = random.randint(
        start,
        end,
    )

    array = []
    for i in range(size):
        while tmp in array:
            tmp = random.randint(
                start,
                end,
            )

        array.append(tmp)

    array.sort()
    return array


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start_idx = 0
        end_idx = len(nums) - 1

        if end_idx < 0 or target > nums[-1] or target < nums[0]:
            return -1

        while start_idx <= end_idx:
            mid_idx = (start_idx + end_idx) // 2

            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] > target:
                end_idx = mid_idx - 1
            elif nums[mid_idx] < target:
                start_idx = mid_idx + 1

        return -1


if __name__ == "__main__":
    obj = Solution()

    assert obj.search(nums=[-1, 0, 3, 5, 9, 12], target=2) == -1

    big_sorted_array = generate_random_sorted_list(size=10, start=-397, end=165)
    target_idx = random.randint(0, 9)
    assert obj.search(nums=big_sorted_array, target=big_sorted_array[target_idx]) == target_idx

    assert obj.search(nums=[2, 3, 4, 5], target=5) == 3
    assert obj.search(nums=[2, 3, 4, 5], target=5) == 3
    assert obj.search(nums=[2, 3, 4, 5], target=2) == 0
    assert obj.search(nums=[2], target=2) == 0
    assert obj.search(nums=[2], target=1) == -1
    assert obj.search(nums=[], target=1) == -1
