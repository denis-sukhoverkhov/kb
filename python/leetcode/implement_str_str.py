class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0

        str_len = len(haystack)
        needle_len = len(needle)
        for i in range(0, str_len + 1 - needle_len):
            if haystack[i:i+needle_len] == needle:
                return i

        return -1


if __name__ == "__main__":
    obj = Solution()

    assert obj.strStr('aaaaa', '') == 0
    assert obj.strStr('hello', 'll') == 2
    assert obj.strStr('aaaaa', 'bba') == -1
