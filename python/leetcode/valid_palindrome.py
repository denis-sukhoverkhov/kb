class Solution:
    def isPalindrome(self, s: str) -> bool:

        lp, rp = 0, len(s)-1

        while lp < rp:
            if not s[lp].isalnum():
                lp += 1
                continue

            if not s[rp].isalnum():
                rp -= 1
                continue

            if s[lp].lower() != s[rp].lower():
                return False

            lp += 1
            rp -= 1

        return True


if __name__ == "__main__":
    obj = Solution()

    assert obj.isPalindrome("9race a car9") is False

    assert obj.isPalindrome("A man, a plan, a canal: Panama") is True