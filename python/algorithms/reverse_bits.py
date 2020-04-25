# https://www.interviewbit.com/problems/reverse-bits/


def reverse(A):
    s = bin(A)

    s = s[-1:1:-1]

    s = s + (32 - len(s)) * "0"

    return int(s, 2)


if __name__ == "__main__":
    assert reverse(3) == 3221225472
