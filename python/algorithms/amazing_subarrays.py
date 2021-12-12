# https://www.interviewbit.com/problems/amazing-subarrays/


def amazing_subarrays(A):
    vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

    ct_amazing_strings = 0

    ln = len(A)
    for k, v in enumerate(A):
        if v in vowel:
            ct_amazing_strings += ln - k

    return ct_amazing_strings % 10003


if __name__ == "__main__":
    st = "ABEC"
    print(amazing_subarrays(st))
