from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        result = []
        for w in words:
            c_s = [i for i in w]
            self.reverseString(c_s)
            result.append(''.join(c_s))

        return ' '.join(result)

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    obj = Solution()

    assert obj.reverseWords("God Ding") == "doG gniD"

    assert obj.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
