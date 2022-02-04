from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrace(s=[], left=0, right=0):
            if len(s) == 2*n:
                result.append(''.join(s))
                return

            if left < n:
                s.append('(')
                backtrace(s, left + 1, right)
                s.pop()

            if right < left:
                s.append(')')
                backtrace(s, left, right + 1)
                s.pop()

        backtrace()

        return result


if __name__ == "__main__":
    obj = Solution()

    assert obj.generateParenthesis(2) == ['(())', '()()']
    assert obj.generateParenthesis(1) == ['()']
