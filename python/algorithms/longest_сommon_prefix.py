# https://www.interviewbit.com/problems/longest-common-prefix/


def longest_common_prefix(A):

    min_len_elem = A[0]

    for i in A:
        if len(min_len_elem) > len(i):
            min_len_elem = i

    res = ""
    idx = 0
    while idx < len(min_len_elem):
        prev_res = res

        for i in A:
            if i[idx] != min_len_elem[idx]:
                break
        else:
            res += min_len_elem[idx]

        idx += 1
        if prev_res == res:
            break

    return res


if __name__ == "__main__":
    A = ["abcdefgh", "aefghijk", "abcefgh"]
    print(longest_common_prefix(A))

    A = ["abab", "ab", "abcd"]
    print(longest_common_prefix(A))
