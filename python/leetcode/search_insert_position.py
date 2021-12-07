class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start_idx = 0
        end_idx = len(nums) - 1

        while start_idx <= end_idx:
            mid = (start_idx + end_idx) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end_idx = mid - 1
            else:
                start_idx = mid + 1

        if start_idx > end_idx:
            return start_idx

        return end_idx


if __name__ == "__main__":
    obj = Solution()

    assert obj.searchInsert(nums=[1], target=0) == 0
    assert obj.searchInsert(nums=[1, 3, 5, 6], target=0) == 0
    assert obj.searchInsert(nums=[1, 3, 5, 6], target=7) == 4
    assert obj.searchInsert(nums=[1, 3, 5, 6], target=2) == 1
    assert obj.searchInsert(nums=[1, 3, 5, 6], target=5) == 2
