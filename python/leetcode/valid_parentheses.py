from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        open_braces = open_close_map.keys()
        close_braces = open_close_map.values()

        close_open_map = {v: k for k, v in open_close_map.items()}

        stack = deque()

        for c in s:
            if c in open_braces:
                stack.append(c)
            elif c in close_braces and len(stack) > 0 and stack[-1] == close_open_map[c]:
                stack.pop()
            else:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    obj = Solution()

    assert obj.isValid('[{()}]')
    assert obj.isValid(')}]') is False
    assert obj.isValid(')') is False
    assert obj.isValid('(') is False
    assert obj.isValid('(]') is False
    assert obj.isValid('()[]{}')
    assert obj.isValid('()')
