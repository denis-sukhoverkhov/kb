from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m1 = {order[i]: i for i in range(len(order))}

        for i in range(len(words)):
            w1 = words[i]
            for j in range(i+1, len(words)):
                w2 = words[j]

                p = 0
                while p < len(w1) and p < len(w2):
                    if m1[w1[p]] > m1[w2[p]]:
                        return False
                    elif m1[w1[p]] < m1[w2[p]]:
                        break
                    p += 1
                else:
                    if len(w1) > len(w2):
                        return False

        return True


if __name__ == "__main__":
    obj = Solution()

    words = ["kuvp", "q"]
    order = "ngxlkthsjuoqcpavbfdermiywz"
    assert obj.isAlienSorted(words, order) is True

    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert obj.isAlienSorted(words, order) is True

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert obj.isAlienSorted(words, order) is False

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert obj.isAlienSorted(words, order) is False
