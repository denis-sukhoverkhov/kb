from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        map_prefixes = {s[:len(s)-i] for i in range(len(s))}

        result = 0
        for w in words:
            if w in map_prefixes:
                result += 1

        return result


if __name__ == "__main__":
    obj = Solution()

    words = ["a", "b", "c", "ab", "bc", "abc"]
    s = "abc"
    assert obj.countPrefixes(words, s) == 3

    words = ["a", "a"]
    s = "aa"
    assert obj.countPrefixes(words, s) == 2