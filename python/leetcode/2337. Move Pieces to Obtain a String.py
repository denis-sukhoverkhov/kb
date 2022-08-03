class Solution:
    def canChange(self, s: str, e: str) -> bool:
        dl = dr = 0
        for ss, ee in zip(s, e):
            if dl > 0 or dr < 0 or ss == 'R' and dl < 0 or ss == 'L' and dr > 0: return False
            dl += int(ss == 'L') - int(ee == 'L')
            dr += int(ss == 'R') - int(ee == 'R')
        return dl == dr == 0


if __name__ == "__main__":
    obj = Solution()

    start = "_L__R__R_"
    target = "L______RR"
    assert obj.canChange(start, target) is True
