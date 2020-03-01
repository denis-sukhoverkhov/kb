
def zeros_in_fact(n):
    """
    https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
    """
    ct = 0

    i = 5
    while n // i >= 1:
        ct += n // i
        i *= 5

    return ct


if __name__ == "__main__":
    # print(zeros_in_fact(7))
    print(zeros_in_fact(9247))
