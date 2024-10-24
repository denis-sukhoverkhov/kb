class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # 1254321
        dig = [int(i) for i in str(n)]

        # 7
        p = len(dig) - 1

        # 1-2-3-4-5
        max_ = dig[p]

        res = -1
        while p >= 0:
            max_ = max(max_, dig[p])

            if dig[p] < max_:

                tmp_arr = dig[p + 1:]
                greater = [i for i in tmp_arr if i > dig[p]]
                min_val = min(greater)
                tmp_arr.remove(min_val)
                tmp_arr.append(dig[p])
                dig[p] = min_val
                tmp_arr.sort()
                res = dig[:p + 1] + tmp_arr
                res = int(''.join([str(i) for i in res]))
                return res if res < 1 << 31 else -1

            p -= 1

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.nextGreaterElement(2147483486) == -1
    assert obj.nextGreaterElement(125431) == 131245
    assert obj.nextGreaterElement(12) == 21
    assert obj.nextGreaterElement(21) == -1
