from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []

        for i in range(len(capacity)):
            diff.append(capacity[i] - rocks[i])

        diff.sort()

        res = 0
        for i in range(len(diff)):
            if diff[i] == 0:
                res += 1
            else:
                tmp = additionalRocks - diff[i]
                if tmp >= 0:
                    additionalRocks -= diff[i]
                    diff[i] = 0
                    res+=1
                else:
                    break

        return res


if __name__ == "__main__":
    obj = Solution()

    capacity = [2, 3, 4, 5]
    rocks = [1, 2, 4, 4]
    additionalRocks = 2
    assert obj.maximumBags(capacity, rocks, additionalRocks) == 3