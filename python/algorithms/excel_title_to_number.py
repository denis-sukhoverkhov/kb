
def title_to_number(A):

    result = 0
    for i in range(len(A)):
        result *= 26
        result += ord(A[i]) - ord('A') + 1

    return result


def convert_to_title(A: int):

    res = []
    while A != 0:
        ost = A % 26
        if ost == 0:
            res.append('Z')
            A = A // 26 - 1
        else:
            res.append(chr(ord('A') + ost - 1))
            A = A // 26

    return "".join(res[::-1])


if __name__ == '__main__':
    print('A=> ', title_to_number('A'))
    print('ZZ=> ', title_to_number('ZZ'))
    print('AB=> ', title_to_number('AB'))
    print('ABC=> ', title_to_number('ABC'))
    print('AAA=> ', title_to_number('AAA'))
    print('AAAB=> ', title_to_number('AAAB'))
    print('AZA=> ', title_to_number('AZA'))
    print('CDA=> ', title_to_number('CDA'), "\n\n")
    print('28=> ', convert_to_title(28))
    print('18280=> ', convert_to_title(18280))
    print('25=> ', convert_to_title(25))
    print('26=> ', convert_to_title(26))
    print('26=> ', convert_to_title(52))
    print('943566=> ', convert_to_title(943566))
