class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        ct_points = 0

        _map = {str(i): set() for i in range(10)}
        for i in range(0, len(rings) - 1, 2):
            color = rings[i]
            point = rings[i+1]
            _map[point].add(color)

        for _, v in _map.items():
            if len(v) == 3:
                ct_points += 1

        return ct_points


if __name__ == "__main__":
    obj = Solution()

    assert obj.countPoints("B0B6G0R6R0R6G9") == 1

    assert obj.countPoints("B0R0G0R9R0B0G0") == 1

    assert obj.countPoints("G4") == 0
