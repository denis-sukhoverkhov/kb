from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        _map = defaultdict(list)
        for i in range(len(strs)):
            angr = strs[i]

            angr_key = [0] * 26

            for c in angr:
                angr_key[ord(c) - ord('a')] += 1

            _map[tuple(angr_key)].append(angr)

        return list(_map.values())


if __name__ == "__main__":
    obj = Solution()

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert obj.groupAnagrams(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
