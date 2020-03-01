
def reverse_integer(n: int):
    # https://www.interviewbit.com/problems/reverse-integer/
    sign = -1 if n < 0 else 1

    ost = abs(n)
    answer = 0
    while ost != 0:
        tmp = ost % 10
        answer = answer * 10 + tmp
        ost = ost // 10

    answer = sign * answer
    max_unsigned_32 = 2**32
    max_32, min_32 = max_unsigned_32 / 2, max_unsigned_32 / 2 * -1
    if answer > max_32 or answer < min_32:
        return 0

    return answer


if __name__ == "__main__":
    print(reverse_integer(123))
    print(reverse_integer(-123))
    print(reverse_integer(-1146467285))
