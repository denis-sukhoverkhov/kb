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
    k = 3
    nums = [1, 2, 3, 4, 5, 6, 7]
    k %= len(nums)
    res = nums[len(nums)-k:] + nums[:len(nums)-k]
    print(res)

    a = 0
    def foo():
        global a

        a += 1
        return a

    print(foo())
    # obj = Solution()
    #
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # assert obj.wordBreak(s, wordDict) is False
    #
    # s = "leetcode"
    # wordDict = ["leet", "code"]
    # assert obj.wordBreak(s, wordDict) is True
