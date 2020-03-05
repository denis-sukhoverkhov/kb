
def add_one_to_number(A):
    number = int("".join([str(i) for i in A]))

    number += 1
    s = str(number)

    return [int(i) for i in s]


if __name__ == "__main__":
    print(add_one_to_number([1, 2, 3]))
    print(add_one_to_number([9, 9, 9]))
