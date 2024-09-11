from math import floor


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:

        ct = 0
        for i in s:
            if i == letter:
                ct += 1

        return floor(ct / len(s) * 100)


if __name__ == "__main__":
    obj = Solution()

    s = "foobar"
    letter = "o"
    assert obj.percentageLetter(s, letter) == 33

    s = "jjjj"
    letter = "k"
    assert obj.percentageLetter(s, letter) == 0
