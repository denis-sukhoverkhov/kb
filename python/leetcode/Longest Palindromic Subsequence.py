class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        res = [[0] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            res[i][i] = 1

        for i in range(1, len(s)+1):
            start = 0
            end = start + i
            while end < len(s):
                if s[start] == s[end]:
                    res[start][end] = 2 + res[start+1][end-1]
                else:
                    if end - start == 1:
                        res[start][end] = 1
                        # continue
                    else:
                        res[start][end] = max(res[start+1][end], res[start][end-1])
                start += 1
                end += 1

        return res[0][-1]


if __name__ == "__main__":
    obj = Solution()

    s = "bbbab"
    assert obj.longestPalindromeSubseq(s) == 4

    s = "cbbd"
    assert obj.longestPalindromeSubseq(s) == 2
