from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:

        stack = []
        for op in ops:
            if op == '+':
                stack.append(stack[-1]+stack[-2])
            elif op == "D":
                stack.append(2*stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)


if __name__ == "__main__":
    obj = Solution()

    ops = ["5", "2", "C", "D", "+"]
    assert obj.calPoints(ops) == 30
