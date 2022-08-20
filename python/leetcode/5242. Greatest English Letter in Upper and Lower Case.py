import string


class Solution:
    def greatestLetter(self, s: str) -> str:
        alph = list(string.ascii_lowercase)

        dct_alph = {alph[i]: i for i in range(len(alph))}

        dct = set()

        max_idx = float('-inf')

        for i in range(len(s)):
            dct.add(s[i])

            if s[i].lower() in dct and s[i].upper() in dct:
                max_idx = max(max_idx, dct_alph[s[i].lower()])

        if max_idx == float('-inf'):
            return ""

        return alph[max_idx].upper()


if __name__ == "__main__":
    obj = Solution()

    assert obj.greatestLetter("lEeTcOdE") == "E"
    assert obj.greatestLetter("arRAzFif") == "R"
    assert obj.greatestLetter("AbCdEfGhIjK") == ""


