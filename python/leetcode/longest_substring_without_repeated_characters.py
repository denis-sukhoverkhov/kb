class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        l = 0

        max_len = 0
        for i in range(len(s)):
            char = s[i]
            while char in set_s:
                set_s.remove(s[l])
                l += 1
            set_s.add(char)
            max_len = max(max_len, len(set_s))
        return max_len


if __name__ == "__main__":
    obj = Solution()

    assert obj.lengthOfLongestSubstring('abcabcbb') == 3