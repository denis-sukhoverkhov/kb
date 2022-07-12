class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)
        m = [[False] * (ls2 + 1) for i in range(ls1 + 1)]

        if ls1+ls2 != len(s3):
            return False

        m[-1][-1] = True
        for i in range(ls1-1, -1, -1):
            m[i][-1] = (s1[i] == s3[i + ls2]) and m[i+1][-1]

        for i in range(ls2-1, -1, -1):
            m[-1][i] = s2[i] == s3[i+ls1] and m[-1][i+1]

        for i in range(ls1 - 1, -1, -1):
            for j in range(ls2 - 1, -1, -1):
                idx = i + j
                if s3[idx] == s1[i] and m[i+1][j] is True:
                    m[i][j] = True
                elif s3[idx] == s2[j] and m[i][j+1] is True:
                    m[i][j] = True

        return m[0][0]


if __name__ == "__main__":
    obj = Solution()

    s1 = "aa"
    s2 = "ab"
    s3 = "abaa"
    assert obj.isInterleave(s1, s2, s3) is True

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    assert obj.isInterleave(s1, s2, s3) is True

    s1 = "bbbcc"
    s2 = "bbaccbbbabcacc"
    s3 = "bbbbacbcccbcbabbacc"
    assert obj.isInterleave(s1, s2, s3) is False

    s1 = ""
    s2 = ""
    s3 = "a"
    assert obj.isInterleave(s1, s2, s3) is False

    s1 = ""
    s2 = ""
    s3 = ""
    assert obj.isInterleave(s1, s2, s3) is True

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    assert obj.isInterleave(s1, s2, s3) is False

