class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1, p2 = 0, 0

        res = []
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                res.append(word1[p1])
                p1 += 1

            if p2 < len(word2):
                res.append(word2[p2])
                p2 += 1

        return ''.join(res)


if __name__ == "__main__":
    obj = Solution()

    word1 = "abc"
    word2 = "pqr"
    assert obj.mergeAlternately(word1, word2) == 'apbqcr'

    word1 = "ab"
    word2 = "pqrs"
    assert obj.mergeAlternately(word1, word2) == 'apbqrs'

    word1 = "abcd"
    word2 = "pq"
    assert obj.mergeAlternately(word1, word2) == 'apbqcd'