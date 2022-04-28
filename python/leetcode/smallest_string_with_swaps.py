from collections import defaultdict
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        p = list(range(len(s)))

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])

            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px != py:
                p[py] = px

        for x, y in pairs:
            union(x, y)

        dct = defaultdict(list)
        for idx, el in enumerate(p):
            dct[find(el)].append(idx)

        result = list(s)
        for k, v in dct.items():
            chars = [s[i] for i in v]
            chars.sort()

            for idx, char in zip(v, chars):
                result[idx] = char

        return ''.join(result)


if __name__ == "__main__":
    obj = Solution()

    s = "ckalujkb"
    pairs = [[0, 3], [2, 5], [7, 2], [2, 3], [5, 7], [1, 4]]
    assert obj.smallestStringWithSwaps(s, pairs) == 'akbcujkl'

    s = "dcab"
    pairs = [[0, 3], [1, 2], [0, 2]]
    assert obj.smallestStringWithSwaps(s, pairs) == 'abcd'

    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    assert obj.smallestStringWithSwaps(s, pairs) == 'bacd'
