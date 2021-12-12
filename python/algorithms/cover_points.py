def cover_points(A, B):

    resp = 0
    for i in range(len(A) - 1):
        x, y = A[i], B[i]

        next_x = A[i + 1]
        next_y = B[i + 1]

        resp += max(abs(x - next_x), abs(y - next_y))

    return resp


if __name__ == "__main__":
    A = [0, 0, 1]
    B = [0, 1, 2]
    print(cover_points(A, B))
