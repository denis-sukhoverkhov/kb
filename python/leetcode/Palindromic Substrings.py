class Solution:
    def countSubstrings(self, s: str) -> int:

        palindromes = {(i, i) for i in range(len(s))}

        for ln in range(2, len(s) + 1):
            for i in range(len(s) - ln + 1):
                first = i
                last = i + ln - 1
                substr = (i + 1, last - 1)
                if substr[0] > substr[1]:
                    substr = None
                if s[first] == s[last] \
                        and (not substr or substr in palindromes):

                    palindromes.add((first, last))

        return len(palindromes)


if __name__ == "__main__":
    obj = Solution()

    s = "aaaaa"
    assert obj.countSubstrings(s) == 15

    s = "aaa"
    assert obj.countSubstrings(s) == 6

    s = "abc"
    assert obj.countSubstrings(s) == 3


