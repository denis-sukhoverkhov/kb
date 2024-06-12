class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1]
        max_len = 0
        for i in range(len(s)):

            if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
                max_len = max(max_len, i - stack[-1])
                continue

            stack.append(i)
        return max_len


if __name__ == "__main__":
    obj = Solution()

    s = ")()())()()("
    assert obj.longestValidParentheses(s) == 4

    s = "()(()"
    assert obj.longestValidParentheses(s) == 2

    s = "(((((("
    assert obj.longestValidParentheses(s) == 0

    s = "()()()))"
    assert obj.longestValidParentheses(s) == 6

    s = ""
    assert obj.longestValidParentheses(s) == 0

    s = ")()())"
    assert obj.longestValidParentheses(s) == 4

    s = "(()"
    assert obj.longestValidParentheses(s) == 2
