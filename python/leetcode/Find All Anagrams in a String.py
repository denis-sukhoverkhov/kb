from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)

        p_len = len(p)
        s_count = Counter(s[:p_len])
        print(p_count, s_count)

        result = [0] if p_count == s_count else []
        print(result)

        l = 0
        for r in range(p_len, len(s)):
            s_count[s[r]] += 1
            s_count[s[l]] -= 1

            if s_count[s[l]] == 0:
                del s_count[s[l]]

            l += 1

            if s_count == p_count:
                result.append(l)

        return result


if __name__ == "__main__":
    obj = Solution()

    s = "cbaebabacd"
    p = "abc"
    assert obj.findAnagrams(s, p) == [0, 6]
