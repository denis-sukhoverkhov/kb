# https://www.interviewbit.com/problems/evaluate-expression/

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):

        op_mapper = {
            "/": "//",
            "+": "+",
            "-": "-",
            "*": "*",
        }
        st = []
        for i in A:
            if i in ("/", "+", "-", "*"):
                second = st.pop()
                first = st.pop()
                st.append(eval(f"{first} {op_mapper[i]} {second}"))
            else:
                st.append(i)

        return st[-1]


if __name__ == "__main__":
    s = Solution()
    A = ["2", "1", "+", "3", "*"]

    assert s.evalRPN(A) == 9

    A = ["4", "13", "5", "/", "+"]
    assert s.evalRPN(A) == 6
