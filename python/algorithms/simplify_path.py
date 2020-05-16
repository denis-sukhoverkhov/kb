class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):

        st = []

        i = 0
        len_a = len(A)
        while i < len_a:
            dir_str = ""

            while i < len_a and A[i] == '/':
                i += 1

            while i < len_a and A[i] != '/':
                dir_str += A[i]
                i += 1

            if dir_str == "..":
                if len(st):
                    st.pop()

            elif dir_str == ".":
                continue
            else:
                st.append(dir_str)

            i += 1

        st1 = st[::-1]

        res = "/"
        while st1:
            poped = st1.pop()

            if res[-1] != '/':
                res += '/'

            res+=poped
        return res



if __name__ == "__main__":
    A = "/a/./b/../../c/"
    s = Solution()
    assert s.simplifyPath(A) == "/c"

    A = "/home/"
    s = Solution()
    assert s.simplifyPath(A) == "/home"
