from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        m = defaultdict(int)

        for i in range(len(num)):
            m[num[i]] += 1

        for i in range(len(num)):
            if m[str(i)] != int(num[i]):
                return False
        return True


if __name__ == "__main__":
    obj = Solution()

    num = "1210"
    assert obj.digitCount(num) is True
