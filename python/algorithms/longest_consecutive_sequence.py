class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        m = set(A)

        max = 0
        for i in A:
            if i - 1 not in m:
                tmp = i
                tmp_max = 0
                while tmp in m:
                    tmp_max += 1
                    tmp += 1
                if tmp_max > max:
                    max = tmp_max

        return max


if __name__ == "__main__":
    s = Solution()

    A = [100, 4, 200, 1, 3, 2]
    assert s.longestConsecutive(A) == 4
