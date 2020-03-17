
def generateMatrix(A):

    matrix = [[0]*A for i in range(A)]

    ''' k - starting row index 
            m - ending row index 
            l - starting column index 
            n - ending column index 
    '''

    k = 0
    l = 0
    m = A - 1
    n = m
    value = 1
    while k <= m and l <= n:

        for i in range(l, n+1):
            matrix[k][i] = value
            value+=1

        k += 1

        for i in range(k, m+1):
            matrix[i][n] = value
            value+=1
        n -= 1

        for i in range(n, l-1, -1):
            matrix[m][i] = value
            value +=1

        m -= 1

        for i in range(m, k - 1, -1):
            matrix[i][l] = value
            value += 1
        l += 1

    return matrix


if __name__ == "__main__":
    A = 5
    res = generateMatrix(A)

    for i in res:
        print(i)
