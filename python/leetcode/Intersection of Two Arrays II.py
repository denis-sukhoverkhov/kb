from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = defaultdict(int)
        for i in nums1:
            m1[i] += 1

        m2 = defaultdict(int)
        for i in nums2:
            m2[i] += 1

        res = []
        for i in m1:
            m1_ct = m1.get(i)
            m2_ct = m2.get(i)

            if not m1_ct or not m2_ct:
                continue

            res += [i] * min(m1_ct, m2_ct)

        return res


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert obj.intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert obj.intersect(nums1, nums2) == [4, 9]
