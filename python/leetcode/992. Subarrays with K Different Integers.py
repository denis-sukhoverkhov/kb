

from collections import Counter
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        res = l_far = l_near = 0
        m = Counter()
        for r in range(len(nums)):
            m[nums[r]] += 1

            while len(m) > k:
                m[nums[l_near]] -= 1

                if m[nums[l_near]] == 0:
                    m.pop(nums[l_near])
                
                l_near += 1
                l_far = l_near

            while m[nums[l_near]] > 1:
                m[nums[l_near]] -= 1 
                l_near += 1   


            if len(m) == k:
                res += l_near - l_far + 1
        
        return res

if __name__ == "__main__":
    obj = Solution()

    res = obj.subarraysWithKDistinct([1,2,1,2,3],2)
    assert res == 7, "actual: %s" % res

    res = obj.subarraysWithKDistinct([1,2,1,3,4], 3)
    assert res == 3, "actual: %s" % res