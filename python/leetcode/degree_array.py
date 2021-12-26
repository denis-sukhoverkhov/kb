class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _map = {}
        for idx, v in enumerate(nums):
            if v in _map:
                _map[v]['ct'] += 1
                _map[v]['end_idx'] = idx
            else:
                _map[v] = {
                    'ct': 1,
                    'start_idx': idx,
                    'end_idx': idx,
                }

        max_value = nums[0]
        min_length = len(nums)
        for k, v in _map.items():
            current_length = v['end_idx'] - v['start_idx'] + 1
            if _map[max_value]['ct'] < v['ct']:
                max_value = k
                min_length = current_length
            elif _map[max_value]['ct'] == v['ct']:
                if current_length < min_length:
                    max_value = k
                    min_length = current_length

        return min_length


if __name__ == "__main__":
    obj = Solution()

    assert obj.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6

    assert obj.findShortestSubArray([1, 2, 2, 3, 1]) == 2
