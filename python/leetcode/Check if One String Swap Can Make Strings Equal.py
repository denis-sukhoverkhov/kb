class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if set(s1) != set(s2):
            return False

        diff_s1 = ''
        diff_s2 = ''
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_s1 += s1[i]
                diff_s2 += s2[i]

                if len(diff_s1) > 2:
                    return False

        if len(diff_s1) not in (0, 2):
            return False

        if set(diff_s1) != set(diff_s2):
            return False

        return True


if __name__ == "__main__":
    obj = Solution()

    s1 = "bankb"
    s2 = "kannb"
    assert obj.areAlmostEqual(s1, s2) is False

    s1 = "caa"
    s2 = "aaz"
    assert obj.areAlmostEqual(s1, s2) is False

    s1 = "bank"
    s2 = "kanb"
    assert obj.areAlmostEqual(s1, s2) is True

    s1 = "attack"
    s2 = "defend"
    assert obj.areAlmostEqual(s1, s2) is False

    s1 = "kelb"
    s2 = "kelb"
    assert obj.areAlmostEqual(s1, s2) is True
