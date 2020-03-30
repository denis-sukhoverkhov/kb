# https://www.interviewbit.com/problems/palindrome-string/


def is_palindrom(A):

    alphabet = [chr(i) for i in range(ord('A'), ord('A') + 26)] + [chr(i) for i in range(ord('a'), ord('a') + 26)]
    numbers = [str(i) for i in range(10)]

    str_alph = []
    for i in A:
        if i in alphabet:
            str_alph.append(i.lower())
        elif i in numbers:
            str_alph.append(i)

    ln = len(str_alph)
    i = 0
    while i < ln / 2:
        if str_alph[i] != str_alph[ln-1-i]:
            return 0
        i+=1

    return 1


if __name__ == "__main__":

    str1 = "A man, a plan, a canal: Panama"
    print(is_palindrom(str1))

    str1 = "mam"
    print(is_palindrom(str1))

    str1 = "ab"
    print(is_palindrom(str1))

    str1 = ""
    print(is_palindrom(str1))

    str1 = "1a2"
    print(is_palindrom(str1))
