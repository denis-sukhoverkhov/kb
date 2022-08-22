class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        current = 0
        ln = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                ln += 1
                continue

            tmp = (1 << (len(s)-i-1))

            if (current | tmp) > k:
                continue

            current |= tmp
            ln += 1

        return ln


if __name__ == "__main__":
    obj = Solution()

    s = "111100010000011101001110001111000000001011101111111110111000011111011000010101110100110110001111001001011001010011010000011111101001101000000101101001110110000111101011000101"
    k = 11713332
    assert obj.longestSubsequence(s, k) == 96

    # s = "1001010"
    # k = 5
    # assert obj.longestSubsequence(s, k) == 5
    #
    # s = "00101001"
    # k = 1
    # assert obj.longestSubsequence(s, k) == 6
