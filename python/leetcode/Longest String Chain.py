from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda k: len(k))

        dp = [1] * len(words)

        mx_val = 1
        for i in range(len(words) - 2, -1, -1):
            w1 = words[i]

            tmp = 0
            for j in range(i + 1, len(words)):
                w2 = words[j]

                if abs(len(w1) - len(w2)) > 1:
                    break

                if len(w1) == len(w2) or tmp > 1 + dp[j]:
                    continue

                if self.is_predecessor(w1, w2):
                    tmp = max(tmp, dp[j])

            dp[i] += tmp
            mx_val = max(mx_val, dp[i])

        return mx_val

    def is_predecessor(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1

        for i in range(len(s2)):
            tmp_str = s2[:i] + s2[i + 1:]
            if s1 == tmp_str:
                return True

        return False

    # def get_count_different_symbols(self, s1, s2):
    #     if len(s1) > len(s2):
    #         s1, s2 = s2, s1
    #
    #     p1 = 0
    #     p2 = 0
    #
    #     ct = 0
    #     while p1 < len(s1) or p2 < len(s2):
    #         if ct > 1:
    #             break
    #
    #         ch1 = s1[p1] if p1 < len(s1) else ''
    #         ch2 = s2[p2] if p2 < len(s2) else ''
    #         if ch1 != ch2:
    #             p2 += 1
    #             ct += 1
    #             continue
    #
    #         p1 += 1
    #         p2 += 1
    #     return ct


if __name__ == "__main__":
    obj = Solution()

    words = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh",
             "gr", "grukmj", "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx",
             "gru"]
    assert obj.longestStrChain(words) == 7

    words = ["abcd", "dbqca"]
    assert obj.longestStrChain(words) == 1

    words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
    assert obj.longestStrChain(words) == 5

    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    assert obj.longestStrChain(words) == 4

    words = ["a", "a"]
    assert obj.longestStrChain(words) == 1
