class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            chunks = [s[i:i+k] for i in range(0, len(s), k)]

            sums = []
            for chunk in chunks:
                sums.append(str(sum([int(i) for i in chunk])))

            s = ''.join(sums)

        return s


if __name__ == "__main__":
    obj = Solution()

    s = "11111222223"
    k = 3
    assert obj.digitSum(s, k) == '135'