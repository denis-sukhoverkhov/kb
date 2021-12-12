# https://www.interviewbit.com/problems/length-of-last-word/


def length_of_last_word(A):

    start_pos = 0
    end_word = False
    end_pos = 0
    for i in range(len(A)):
        if A[i] == " ":
            start_word = False
            end_word = True
            end_pos = i
        else:
            start_word = True

        if start_word and end_word:
            start_pos = i
            end_word = False

    end_pos = len(A) if end_pos <= start_pos else end_pos
    return len(A[start_pos:end_pos].strip())


if __name__ == "__main__":
    s = "Hello World"
    print(length_of_last_word(s))

    s = ""
    print(length_of_last_word(s))

    s = "Hello World "
    print(length_of_last_word(s))

    s = "Hello World  "
    print(length_of_last_word(s))
