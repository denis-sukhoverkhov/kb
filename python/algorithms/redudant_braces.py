class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        st = []

        for i in A:
            if i == ")":
                elem = st.pop()
                flag = True
                while elem != "(":
                    if elem in ("+", "*", "/", "-"):
                        flag = False
                    elem = st.pop()

                if flag:
                    return 1
            else:
                st.append(i)

        return 0


if __name__ == "__main__":
    s = Solution()
    A = "((a + b))"
    assert s.braces(A) == 1

    A = "(a + (a + b))"
    assert s.braces(A) == 0
