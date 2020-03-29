# https://www.interviewbit.com/problems/count-and-say/


def count_and_stay(A):

    if A == 0:
        return ''

    tmp = str(1)
    for i in range(1, A):
        next_tmp = ''
        t = ''
        for j in tmp:
            if t and j not in t:
                next_tmp += str(len(t)) + str(int(t[0]))
                t = ''
            t += j

        if t:
            next_tmp += str(len(t)) + str(int(t[0]))
            # t = ''

        tmp = next_tmp

    return tmp


if __name__ == '__main__':
    a = 1
    print(count_and_stay(a))

    a = 4
    print(count_and_stay(a))

    a = 10
    print(count_and_stay(a))
