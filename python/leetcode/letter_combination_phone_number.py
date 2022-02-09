from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h_m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        result = []

        def backtrace(idx: int, curr_str: str):

            if len(curr_str) == len(digits):
                result.append(curr_str)
                return

            for s in h_m[digits[idx]]:
                backtrace(idx+1, curr_str + s)

        if digits:
            backtrace(0, "")

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    assert obj.letterCombinations("") == []
