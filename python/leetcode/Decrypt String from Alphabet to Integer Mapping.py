class Solution:
    def freqAlphabets(self, s: str) -> str:
        m1 = {i: chr(ord('a')+i) for i in range(26)}

        res = ''
        stack = []

        pointer = 0
        while stack or pointer < len(s):
            if pointer < len(s) and s[pointer] == '#' and len(stack) < 3:
                number = stack.pop()
                number += stack.pop()
                res += m1[int(number[::-1])-1]
                pointer += 1
            elif len(stack) == 3 or pointer >= len(s):
                res += m1[int(stack.pop(0))-1]
            elif pointer < len(s):
                stack.append(s[pointer])
                pointer += 1

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.freqAlphabets("1326#") == 'acz'

    assert obj.freqAlphabets("10#11#12") == "jkab"
