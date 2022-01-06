from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = defaultdict(int)

        for i in s1:
            s1_map[i] += 1

        s2_max_idx = len(s2)
        p1, p2 = 0, len(s1) - 1

        while p1 <= s2_max_idx or p1 <= s2_max_idx:
            tmp_s2_map = defaultdict(int)
            for i in s2[p1: p2 + 1]:
                tmp_s2_map[i] += 1

            if s1_map == tmp_s2_map:
                return True
            p1 += 1
            p2 += 1

        return False


if __name__ == "__main__":
    obj = Solution()

    assert obj.checkInclusion('ab', 'eidboaoo') is False

    assert obj.checkInclusion('ab', 'eidbaooo') is True

