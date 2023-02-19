class Solution:
    def largestGoodInteger(self, num: str) -> str:

        max_num = ''
        current_contiguous_num = ''
        for i in num:
            if i not in current_contiguous_num:
                current_contiguous_num = ''

            current_contiguous_num += i

            if len(current_contiguous_num) == 3:
                if not max_num or int(max_num) < int(current_contiguous_num):
                    max_num = current_contiguous_num

        return max_num


if __name__ == "__main__":
    obj = Solution()

    num = "6777133339"
    assert obj.largestGoodInteger(num) == '777'


    num = "2300019"
    assert obj.largestGoodInteger(num) == '000'

    num = "42352338"
    assert obj.largestGoodInteger(num) == ''