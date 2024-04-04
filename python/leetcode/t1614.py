# 1614. Maximum Nesting Depth of the Parentheses
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        
        res = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.pop()
            
            res = max(res, len(stack))


        return res


if __name__ == "__main__":
    obj = Solution()

    s = "(1+(2*3)+((8)/4))+1"
    res = obj.maxDepth(s)
    assert res == 3, "actual: %s" % res
