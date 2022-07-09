from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        # new_arr = []
        for i in range(len(arr)):
            arr[i] = (self.get_number_of_bits(arr[i]), arr[i])

        arr.sort()

        return [i[1] for i in arr]

    def get_number_of_bits(self, number):

        count = 0
        n = number
        while n:
            n &= (n - 1)
            count += 1

        return count


if __name__ == "__main__":
    obj = Solution()

    assert obj.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]) == [1, 2, 4, 8, 16, 32, 64,
                                                                             128, 256, 512, 1024]
    assert obj.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [0, 1, 2, 4, 8, 3, 5, 6, 7]
