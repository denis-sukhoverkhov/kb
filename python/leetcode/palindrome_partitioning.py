from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []
        max_idx = len(s) - 1

        def traceback(i: int):
            if i > max_idx:
                result.append(
                    part.copy()
                )
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s, lp=i, rp=j):
                    part.append(s[i:j + 1])
                    traceback(j + 1)
                    part.pop()

        traceback(0)

        return result

    def is_palindrome(self, s, lp, rp):
        while lp < rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1

        return True


if __name__ == "__main__":
    obj = Solution()

    assert obj.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
