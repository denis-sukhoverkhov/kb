# https://www.interviewbit.com/problems/implement-strstr/


def str_str(A, B):
    res_idx = -1

    if not A or not B or len(B) > len(A):
        return res_idx

    ln_b = len(B)

    for i in range(len(A)):
        if A[i : i + ln_b] == B:
            return i

    return res_idx


if __name__ == "__main__":
    s = "HelloWorld"
    sb = "World"
    print(str_str(s, sb))
