# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def __init__(self, bad_version):
        self.bad_version = bad_version

    def isBadVersion(self, version):
        return version == self.bad_version

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        last_bad_version = -1
        while start <= end:
            mid = (start + end) // 2

            if self.isBadVersion(mid):
                last_bad_version = mid
                end = mid - 1
            else:
                start = mid + 1

        return last_bad_version


if __name__ == "__main__":
    obj = Solution(4)
    assert obj.firstBadVersion(5) == 4

    obj = Solution(1)
    assert obj.firstBadVersion(1) == 1
