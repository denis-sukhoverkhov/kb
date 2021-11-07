
def sum_a_b(a, b):
    return a+b


if __name__ == "__main__":
    with open('input.txt', "r") as fi:
        numbers = fi.readline()

    numbers = numbers.split(' ')
    numbers = [int(i) for i in numbers if i]

    with open('output.txt', 'w') as fo:
        fo.write(str(sum_a_b(*numbers)))
