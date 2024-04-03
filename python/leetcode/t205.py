# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/

from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        for i in range(0, len(s)):
            if s[i] not in m:
                m[s[i]] = t[i]

            if m[s[i]] != t[i]:
                return False
        
        return len(m.keys()) == len(set(m.values()))


if __name__ == "__main__":
    obj = Solution()

    s = "egg"
    t = "add"
    res = obj.isIsomorphic(s, t)
    assert res, "actual: %s" % res

    s = "foo"
    t = "bar"
    res = obj.isIsomorphic(s, t)
    assert res, "actual: %s" % res