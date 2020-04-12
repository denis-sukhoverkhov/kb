# https://www.interviewbit.com/problems/compare-version-numbers/


def compareVersion(A, B):
    a_dig = [int(i) for i in A.split('.') if i]
    b_dig = [int(i) for i in B.split('.') if i]

    max_len = max(len(a_dig), len(b_dig))
    for i in range(max_len):

        a = a_dig[i] if i < len(a_dig) else 0
        b = b_dig[i] if i < len(b_dig) else 0

        if a > b:
            return 1
        elif a < b:
            return -1

    return 0


if __name__ == "__main__":
    assert compareVersion("1.0", "1") == 0
    assert compareVersion("01", "1") == 0
    assert compareVersion("12.13", "1.13") == 1
    assert compareVersion("1.13", "1.13") == 0
    assert compareVersion("1.13", "1.13.4") == -1
    assert compareVersion("", "1.13") == -1
    assert compareVersion("1.13", "") == 1
    assert compareVersion("", "") == 0
    assert compareVersion("2.4", "2.4") == 0
