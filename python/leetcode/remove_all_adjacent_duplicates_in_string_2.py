from typing import List


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack: List[tuple] = []

        for character in s:
            new_count = 1
            if stack:
                char, count = stack[-1]

                if char == character:
                    new_count += count

            stack.append((character, new_count))

            if new_count >= k:
                current_char = character
                while current_char == character:
                    stack.pop()

                    if stack:
                        current_char, _ = stack[-1]
                    else:
                        current_char = None

        return ''.join(i[0] for i in stack)


if __name__ == "__main__":
    obj = Solution()

    s = "deeedbbcccbdaa"
    k = 3
    assert obj.removeDuplicates(s, k) == 'aa'


    s = "abcd"
    k = 2
    assert obj.removeDuplicates(s, k) == 'abcd'