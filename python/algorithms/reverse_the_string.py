# https://www.interviewbit.com/problems/reverse-the-string/


def reverse_the_string(A: str):

    list_of_words = A.split(" ")

    filtered_words = [i for i in list_of_words if i]

    return " ".join(filtered_words[::-1])


if __name__ == "__main__":
    A = "the sky is blue"
    print(reverse_the_string(A))

    A = "this is ib"
    print(reverse_the_string(A))
