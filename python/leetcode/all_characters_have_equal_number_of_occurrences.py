class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        _map = {}
        for i in s:
            if i in _map:
                _map[i] += 1
            else:
                _map[i] = 1

        random_key = s[0]
        ct = _map[random_key]
        for k, v in _map.items():
            if v != ct:
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    assert obj.areOccurrencesEqual("abacbc") is True

    assert obj.areOccurrencesEqual("aaabb") is False
