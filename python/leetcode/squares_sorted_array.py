class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_abs_v = abs(nums[0])
        idx = 0

        for k, v in enumerate(nums):
            if abs(v) < min_abs_v:
                min_abs_v = abs(v)
                idx = k

        if idx == len(nums) - 1:
            r_p = idx
            l_p = r_p - 1
        elif idx == 0:
            l_p = idx
            r_p = idx + 1
        else:
            r_p = idx
            l_p = r_p - 1

        max_r_p = len(nums) - 1
        result = []

        while r_p <= max_r_p or l_p >= 0:

            if r_p > max_r_p:
                l_sq = nums[l_p] ** 2
                result.append(l_sq)
                l_p -= 1
                continue

            if l_p < 0:
                r_sq = nums[r_p] ** 2
                result.append(r_sq)
                r_p += 1
                continue

            l_sq = nums[l_p] ** 2
            r_sq = nums[r_p] ** 2
            if r_sq >= l_sq:
                result.append(l_sq)
                l_p -= 1
            elif r_sq < l_sq:
                result.append(r_sq)
                r_p += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.sortedSquares([-5, -3, -2, -1]) == [1, 4, 9, 25]

    assert obj.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]

    assert obj.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
