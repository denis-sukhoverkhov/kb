# https://www.interviewbit.com/problems/minimum-characters-required-to-make-a-string-palindromic/


def is_palindrom(A):
    ln = len(A)
    i = 0
    while i < ln / 2:
        if A[i] != A[ln - 1 - i]:
            return 0
        i += 1

    return 1


def make_palindromic(A):

    ct = 0
    flag = False

    while len(A):

        if is_palindrom(A):
            flag = True
            break
        else:
            ct += 1
            A = A[:-1]

    if flag:
        return ct

    return 0


if __name__ == "__main__":
    print(make_palindromic("ABC"))
    print(make_palindromic("AAACECAAAA"))
    print(make_palindromic(""))
