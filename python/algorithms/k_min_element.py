def k_min_el(A, B):

    a = sorted(A)

    return a[B - 1]


if __name__ == "__main__":
    A = [2, 1, 4, 3, 2]
    B = 3
    assert k_min_el(A, B) == 2
