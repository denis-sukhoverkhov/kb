from collections import defaultdict


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        m2 = defaultdict(int)
        for i in target:
            m2[i] += 1

        m1 = defaultdict(int)
        for i in s:
            if i in m2:
                m1[i] += 1

        min_val = float('inf')
        for i in m2:
            val = m1.get(i, 0)
            min_val = min(min_val, val // m2[i])

        return min_val


if __name__ == "__main__":
    obj = Solution()

    s = "acc"
    target = "c"
    assert obj.rearrangeCharacters(s, target) == 2

    s = "abbaccaddaeea"
    target = "aaaaa"
    assert obj.rearrangeCharacters(s, target) == 1

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    target = "aaaaaaaaaa"
    assert obj.rearrangeCharacters(s, target) == 10
    #
    #
    s = "codecodecodecode"
    target = "codecode"

    assert obj.rearrangeCharacters(s, target) == 2
    #
    s = "lrnvlcqukanpdnluowenfxquitzryponxsikhciohyostvmkapkfpglzikitwiraqgchxnpryhwpuwpozacjhmwhjvslprqlnxrk"
    target = "woijih"
    assert obj.rearrangeCharacters(s, target) == 2
    #

    s = "acc"
    target = "b"
    assert obj.rearrangeCharacters(s, target) == 0

    s = "ilovecodingonleetcode"
    target = "code"
    assert obj.rearrangeCharacters(s, target) == 2

    s = "abcba"
    target = "abc"
    assert obj.rearrangeCharacters(s, target) == 1
