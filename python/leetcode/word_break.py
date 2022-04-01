from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ln = len(s)

        _map = {len(s): True}
        for i in range(ln-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= ln and s[i:i+len(w)] == w:
                    _map[i] = _map.get(i + len(w), False)
                if _map.get(i):
                    break

        return _map.get(0, False)


if __name__ == "__main__":
    obj = Solution()

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    assert obj.wordBreak(s, wordDict) is False

    s = "leetcode"
    wordDict = ["leet", "code"]
    assert obj.wordBreak(s, wordDict) is True
