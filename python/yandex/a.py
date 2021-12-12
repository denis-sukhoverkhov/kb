def sum_a_b(a, b):
    return a + b


if __name__ == "__main__":
    input = input()

    values = input.split(" ")
    numbers = [int(i) for i in values if i]

    print(sum_a_b(*numbers))
