
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = [[0] * (len(word1) + 1) for i in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            m[0][i] = i

        for i in range(1, len(word2) + 1):
            m[i][0] = i

        # print(m)
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if word2[i - 1] == word1[j - 1]:
                    m[i][j] = m[i - 1][j - 1]
                else:
                    m[i][j] = 1 + min(m[i - 1][j], m[i][j - 1])

        return m[-1][-1]


if __name__ == "__main__":
    obj = Solution()

    word1 = "strike"
    word2 = "op"
    assert obj.minDistance(word1, word2) == 8

    word1 = "leetcode"
    word2 = "etco"
    assert obj.minDistance(word1, word2) == 4

    word1 = "errr"
    word2 = "r"
    assert obj.minDistance(word1, word2) == 3

    word1 = "sea"
    word2 = "eat"
    assert obj.minDistance(word1, word2) == 2
