class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        res = 0

        def traceback(idx, current):
            nonlocal res

            current.append(vowels[idx])

            if len(current) == n:
                res += 1
                return

            for i in range(idx, len(vowels)):
                traceback(i, current)
                current.pop()

        current = []
        for i in range(len(vowels)):
            traceback(i, current)
            current.pop()

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.countVowelStrings(1) == 5
    assert obj.countVowelStrings(2) == 15
    assert obj.countVowelStrings(3) == 35
    assert obj.countVowelStrings(4) == 70
    assert obj.countVowelStrings(5) == 126

