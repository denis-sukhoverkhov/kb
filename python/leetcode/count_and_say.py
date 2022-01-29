class Solution:
    def countAndSay(self, n: int) -> str:

        def traceback(n):
            if n == 1:
                return '1'

            prev_str = traceback(n-1)

            prev = prev_str[0]
            ct = 0
            new_str = ''
            for i in range(0, len(prev_str)):
                if prev_str[i] != prev:
                    new_str += f"{str(ct)}{str(prev_str[i-1])}"
                    ct = 0
                    prev = prev_str[i]
                ct += 1
            else:
                if ct != 0:
                    new_str += f"{str(ct)}{str(prev_str[-1])}"

            return new_str

        res = traceback(n)

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.countAndSay(8) == '1113213211'
    assert obj.countAndSay(7) == '13112221'
    assert obj.countAndSay(6) == '312211'
    assert obj.countAndSay(5) == '111221'
    assert obj.countAndSay(4) == '1211'
    assert obj.countAndSay(3) == '21'
    assert obj.countAndSay(2) == '11'
    assert obj.countAndSay(1) == '1'