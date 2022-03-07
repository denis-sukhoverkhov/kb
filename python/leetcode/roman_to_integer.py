class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {
            "X": 10,
            "I": 1,
            "V": 5,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and _map[s[i]] < _map[s[i+1]]:
                result -= _map[s[i]]
            else:
                result += _map[s[i]]

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.romanToInt('MCMXCIV') == 1994

    assert obj.romanToInt('III') == 3

    assert obj.romanToInt('LVIII') == 58
