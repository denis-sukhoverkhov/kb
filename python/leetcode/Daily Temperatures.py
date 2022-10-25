from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        st = []

        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            val = temperatures[i]

            while st and val > st[-1][0]:
                stack_value, idx = st[-1]
                res[idx] = i - idx
                st.pop()

            st.append((val, i))

        return res


if __name__ == "__main__":
    obj = Solution()

    assert obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
