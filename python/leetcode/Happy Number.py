class Solution:
    def isHappy(self, n: int) -> bool:

        tmp_set = set()
        tmp = n
        while tmp != '1':
            tmp = str(sum([int(i)**2 for i in str(tmp)]))

            if tmp in tmp_set:
                return False

            tmp_set.add(tmp)

        return True


if __name__ == "__main__":
    obj = Solution()

    assert obj.isHappy(19) is True
    assert obj.isHappy(2) is False
