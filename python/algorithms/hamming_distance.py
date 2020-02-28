import itertools


def hamming_distance_simple(A: list):
    pairs = itertools.permutations(A, 2)

    ct = 0
    for pair in pairs:
        if pair[0] < pair[1]:
            x = pair[0] ^ pair[1]

            setbits = 0
            while x > 0:
                setbits += x & 1
                x >>= 1

            ct += setbits * 2

    return ct


def hamming_distance_smart(A: list):
    ans = 0

    for i in range(0, 32):
        count = 0
        n = len(A)
        for j in range(0, n):
            if A[j] & (1 << i):
                count += 1

        ans += count * (n - count) * 2

    return ans % 1000000007


if __name__ == "__main__":
    a = [2, 4, 6]
    # print(hamming_distance_simple(a))
    print(hamming_distance_smart(a))
