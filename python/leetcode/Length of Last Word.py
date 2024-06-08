class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        prev = 0
        current_len = 0
        for i in range(len(s)):
            if s[i] != ' ':
                current_len += 1
            else:
                prev = current_len if current_len else prev
                current_len = 0

        return prev if s[-1] == ' ' else current_len


if __name__ == "__main__":
    obj = Solution()

    assert obj.lengthOfLastWord("   fly me   to   the moon  ") == 4
