from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def helper(strings):
            len_of_first_str = len(strings[0])
            for i in range(len_of_first_str):
                for s in strings:
                    if i == len(s) or s[i] != strings[0][i]:
                        return i

        idx = helper(strs)

        return strs[0][:idx]


if __name__ == "__main__":
    obj = Solution()

    assert obj.longestCommonPrefix(["dog", "racecar", "car"]) == ''

    assert obj.longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
