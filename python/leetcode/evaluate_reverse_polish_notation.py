from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i in "+-*/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(eval(f'{val1} {i} {val2}')))
            else:
                stack.append(int(i))

        return stack[-1]


if __name__ == "__main__":
    obj = Solution()

    assert obj.evalRPN(["2", "1", "+"]) == 3

    assert obj.evalRPN(["2", "1", "+", "3", "*"]) == 9
