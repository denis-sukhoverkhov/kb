from collections import Counter
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        m = []
        for i in range(0, len(garbage)):
            m.append(Counter(garbage[i]))
        res = sum(m[0].values())

        travel_prefix = [travel[0]]
        for j in range(1, len(travel)):
            travel_prefix.append(travel_prefix[j - 1] + travel[j])
        # print(travel_prefix)
        # last_car_position

        car_positions = {
            'M': 0,
            'G': 0,
            'P': 0,
        }
        for i in range(1, len(m)):
            values = m[i].values()
            # keys = m[i].kets()
            res += sum(values)

            for k, v in m[i].items():
                res += travel_prefix[i - 1]

                if car_positions[k] > 0:
                    res -= travel_prefix[car_positions[k] - 1]

                car_positions[k] = i

        return res


if __name__ == "__main__":
    obj = Solution()
    assert obj.garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]) == 21

    assert obj.garbageCollection(["MMM", "PGM", "GP"], [3, 10]) == 37
