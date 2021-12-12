# https://www.interviewbit.com/problems/roman-to-integer/


def roman_to_integer(A):
    map = {
        "X": 10,
        "I": 1,
        "V": 5,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    sum = 0
    tmp_sum = 0
    skip = False
    for i in range(0, len(A)):
        if skip:
            skip = False
            continue

        if i == len(A) - 1:
            sum += map[A[i]] + tmp_sum
            tmp_sum = 0
            continue

        if map[A[i]] > map[A[i + 1]]:
            sum += map[A[i]] + tmp_sum
            tmp_sum = 0
            continue

        if map[A[i]] == map[A[i + 1]]:
            tmp_sum += map[A[i]]
            continue

        if map[A[i]] < map[A[i + 1]]:
            tmp_sum += map[A[i]]
            sum += map[A[i + 1]] - tmp_sum
            tmp_sum = 0
            skip = True

    return sum


if __name__ == "__main__":
    s = "XIV"
    print(roman_to_integer(s))

    s = "XX"
    print(roman_to_integer(s))

    s = "MMVI"
    print(roman_to_integer(s))

    s = "MMXXV"
    print(roman_to_integer(s))

    s = "MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCMXXXI"
    print(roman_to_integer(s))

    s = "MMMCCLXXXVII"
    print(roman_to_integer(s))

    s = "CMVI"
    print(roman_to_integer(s))
