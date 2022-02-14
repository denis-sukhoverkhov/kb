from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last_interval = result[-1]
            right_border = last_interval[1]

            curr_interval = intervals[i]
            if right_border >= curr_interval[0]:
                result[-1][1] = max(result[-1][1], curr_interval[1])
            else:
                result.append(curr_interval)

        return result


if __name__ == "__main__":
    obj = Solution()

    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert obj.merge(intervals) == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    assert obj.merge(intervals) == [[1, 5]]
