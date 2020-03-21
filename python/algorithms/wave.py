

def wave(A):

    A.sort()
    res = []
    tmp = None
    for i in range(len(A)):
        if i == 0 or i % 2 == 0 and tmp is None:
            tmp = A[i]
        else:
            res.append(A[i])
            res.append(tmp)
            tmp = None

    if tmp is not None:
        res.append(tmp)

    return res


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    print(wave(A))

    A = [ 5, 1, 3, 2, 4 ]
    print(wave(A))
