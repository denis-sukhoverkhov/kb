from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)
        t_counter = Counter(t)

        for i in t_counter:
            if t_counter.get(i) != s_counter.get(i):
                return i


if __name__ == "__main__":
    obj = Solution()

    s = "abcd"
    t = "abcde"
    assert obj.findTheDifference(s, t) == 'e'
