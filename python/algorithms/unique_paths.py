# https://www.interviewbit.com/problems/grid-unique-paths/


def unique_paths_recursive(A, B):
    "exponential complexity"
    if A == 1 or B == 1:
        return 1

    return unique_paths_recursive(A - 1, B) + unique_paths_recursive(A, B - 1)


def unique_paths_table(A, B):
    matrix = [[0] * B for _ in range(A)]

    matrix[0] = [1] * B

    for i in range(A):
        matrix[i][0] = 1

    for i in range(1, A):
        for j in range(1, B):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]

    return matrix[A - 1][B - 1]


if __name__ == "__main__":
    print(unique_paths_recursive(3, 3))
    print(unique_paths_table(3, 3))
    pass
