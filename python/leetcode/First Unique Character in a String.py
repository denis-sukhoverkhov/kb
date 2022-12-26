from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        m = Counter(s)

        for i in range(len(s)):
            if m[s[i]] == 1:
                return i

        return -1


if __name__ == "__main__":
    obj = Solution()

    s = "leetcode"
    assert obj.firstUniqChar(s) == 0
