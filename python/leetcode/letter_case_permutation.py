from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        result = []
        len_str = len(s)

        def traceback(idx, current):

            if idx >= len_str:
                result.append(current)
                return

            if s[idx].isalpha():
                traceback(idx + 1, current + s[idx].lower())
                traceback(idx + 1, current + s[idx].upper())
            else:
                traceback(idx + 1, current + s[idx])

        traceback(0, '')

        return result


if __name__ == "__main__":
    obj = Solution()

    s = "a1b2"
    assert obj.letterCasePermutation(s) == ["a1b2", "a1B2", "A1b2", "A1B2"]
