from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        m1 = defaultdict(int)
        for i in range(len(s)):
            m1[s[i]] += 1

        m2 = defaultdict(int)
        for i in range(len(t)):
            m2[t[i]] += 1

        if len(m1) != len(m2):
            return False

        for ch in m1:
            if m1[ch] != m2.get(ch):
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    s = "a"
    t = "ab"
    assert obj.isAnagram(s, t) is False

    s = "anagram"
    t = "nagaram"
    assert obj.isAnagram(s, t) is True

    s = "rat"
    t = "car"
    assert obj.isAnagram(s, t) is False
