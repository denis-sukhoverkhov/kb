from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for i in ransomNote:
            if r[i] > m.get(i, 0):
                return False

        return True


if __name__ == "__main__":
    obj = Solution()

    ransomNote = "a"
    magazine = "b"
    assert obj.canConstruct(ransomNote, magazine) is False

    ransomNote = "aa"
    magazine = "ab"
    assert obj.canConstruct(ransomNote, magazine) is False

    ransomNote = "aa"
    magazine = "aab"
    assert obj.canConstruct(ransomNote, magazine) is True