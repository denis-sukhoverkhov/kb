def get_row(A):
    # https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
    ln = A + 1
    matrix = [[0 for j in range(ln)] for i in range(ln)]

    for row in range(ln):
        for col in range(row + 1):
            if col == 0 or row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = matrix[row - 1][col - 1] + matrix[row - 1][col]

    return matrix[-1]


def print_pascal_triangle(A):
    # https://www.interviewbit.com/problems/pascal-triangle/
    ln = A
    matrix = [[] for _ in range(ln)]

    for row in range(ln):
        for col in range(row + 1):
            if col == 0 or row == col:
                matrix[row].append(1)
            else:
                matrix[row].append(matrix[row - 1][col - 1] + matrix[row - 1][col])

    return matrix


if __name__ == "__main__":
    print(get_row(1))
    print(get_row(2))
    print(get_row(3))
    print(get_row(4))
    print(get_row(5))

    print(print_pascal_triangle(5))
