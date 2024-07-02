from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bit_words = []
        for i in range(len(words)):
            s = set(words[i])

            res = 0
            for k in s:
                tmp = 1 << (ord(k) - 97)
                res |= tmp

            bit_words.append(res)

        max_power_of_length = 0
        for i in range(len(bit_words)):
            for j in range(i + 1, len(bit_words)):
                if bit_words[i] & bit_words[j] == 0:
                    max_power_of_length = max(
                        max_power_of_length, len(words[i]) * len(words[j])
                    )

        return max_power_of_length


if __name__ == "__main__":
    obj = Solution()

    words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
    assert obj.maxProduct(words) == 4

    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
    assert obj.maxProduct(words) == 16
