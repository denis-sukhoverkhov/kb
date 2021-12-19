class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = nums[0]
        temp_sum = nums[0]

        for i in nums[1:]:
            temp_sum = max(i, sum([temp_sum, i]))
            max_sum = max(temp_sum, max_sum)

        return max_sum


if __name__ == "__main__":
    obj = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert obj.maxSubArray(nums) == 6

    nums = [5, 4, -1, 7, 8]
    assert obj.maxSubArray(nums) == 23

    nums = [1]
    assert obj.maxSubArray(nums) == 1
