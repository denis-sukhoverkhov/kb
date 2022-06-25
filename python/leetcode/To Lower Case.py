class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []

        for i in s:
            if 65 <= ord(i) <= 90:
                res.append(chr(ord(i) + 32))
            else:
                res.append(i)

        return ''.join(res)


if __name__ == "__main__":
    obj = Solution()
    s = "Hello"
    assert obj.toLowerCase(s) == 'hello'

    s = "al&phaBET"
    assert obj.toLowerCase(s) == "al&phabet"

