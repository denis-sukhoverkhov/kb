class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_stack(s):
            stack = []
            for i in s:
                if i == '#':
                    if stack:
                        stack.pop()
                    continue

                stack.append(i)

            return stack

        a1 = get_stack(s)
        a2 = get_stack(t)

        return a1 == a2


if __name__ == "__main__":
    obj = Solution()

    s = "a##c"
    t = "#a#c"
    assert obj.backspaceCompare(s, t) is True

    s = "a#c"
    t = "b"
    assert obj.backspaceCompare(s, t) is False

    s = "ab#c"
    t = "ad#c"
    assert obj.backspaceCompare(s, t) is True
