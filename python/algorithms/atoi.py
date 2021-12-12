def atoi(A):
    m = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }

    sign = 1
    res = 0

    for idx in range(len(A)):
        if A[idx] == "-" and idx == 0:
            sign = -1
            continue

        if A[idx] == "+" and idx == 0:
            continue

        val = m.get(A[idx])
        if val is None:
            break

        res = res * 10 + m[A[idx]]

    if sign == -1:
        res *= -1

    if res > 2147483647:
        return 2147483647

    if res < -2147483648:
        return -2147483648

    return res


if __name__ == "__main__":
    print(atoi("44024E11 G24 378556582G0467E 6 613 1 2173 9829 5K5H099 2Q 458890732 94 0"))  # 44024
    # print(atoi(''))  # 0
    # print(atoi('1'))  # 1
    # print(atoi('1 '))  # 1
    # print(atoi('1f'))  # 1
    # print(atoi('421421342314231421341234123421'))  # 2147483647
    print(atoi("-421421342314231421341234123421"))  # -2147483648
    print(atoi("-421421342-314231421341234123421"))  # -2147483648
    print(atoi("+7"))  # 7
