
def prime_sum(A):
    """
    https://www.interviewbit.com/problems/prime-sum/
    :param A:
    :return:
    """
    prime = [True for _ in range(A + 1)]
    p = 2

    while p * p <= A:
        if prime[p]:
            for i in range(p * p, A + 1, p):
                prime[i] = False
        p += 1

    for p in range(2, A):
        if prime[p] and prime[A-p]:
            return [p, A-p]


if __name__ == '__main__':
    print(prime_sum(16777214))
