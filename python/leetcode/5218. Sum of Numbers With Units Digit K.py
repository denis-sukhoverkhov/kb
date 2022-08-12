class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        if num == k:
            return 1

        if num < k:
            return -1

        if k == 0 and num % 10 == 0:
            return 1

        if k == 0 and num % 10 != 0:
            return -1

        cache = set()

        curr = 0
        while num not in cache and num >= 0:
            if num % 10 == k:
                break

            cache.add(num % 10)
            num = num - k
            curr += 1

            if num < 0:
                return -1
        else:
            return -1

        return curr + 1


if __name__ == "__main__":
    obj = Solution()

    num = 14
    k = 4
    assert obj.minimumNumbers(num, k) == 1

    num = 18
    k = 7
    assert obj.minimumNumbers(num, k) == -1

    num = 7
    k = 2
    assert obj.minimumNumbers(num, k) == -1

    num = 5
    k = 1
    assert obj.minimumNumbers(num, k) == 5

    num = 2
    k = 8
    assert obj.minimumNumbers(num, k) == -1

    num = 1
    k = 1
    assert obj.minimumNumbers(num, k) == 1

    num = 37
    k = 2
    assert obj.minimumNumbers(num, k) == -1

    num = 58
    k = 3
    assert obj.minimumNumbers(num, k) == 6

    num = 58
    k = 9
    assert obj.minimumNumbers(num, k) == 2

    num = 0
    k = 7
    assert obj.minimumNumbers(num, k) == 0
