
def title_to_number(A):

    result = 0
    for i in range(len(A)):
        result *= 26
        result += ord(A[i]) - ord('A') + 1

    return result


if __name__ == '__main__':
    print(title_to_number('A'))
    print(title_to_number('AA'))
    print(title_to_number('AB'))
    print(title_to_number('ABC'))
    print(title_to_number('AAA'))
    print(title_to_number('AAAB'))
    print(title_to_number('AZA'))
    print(title_to_number('CDA'))
