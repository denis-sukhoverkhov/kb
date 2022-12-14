class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)

        res = 0
        ln = len(num_str)
        for i in range(ln - k + 1):
            curr = int(num_str[i:i+k])

            if curr and num % curr == 0:
                res += 1

        return res


if __name__ == "__main__":
    obj = Solution()

    num = 430043
    k = 2
    assert obj.divisorSubstrings(num, k) == 2

    num = 240
    k = 2
    assert obj.divisorSubstrings(num, k) == 2
