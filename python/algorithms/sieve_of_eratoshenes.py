def sieve_of_eratosthenes(number: int):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for _ in range(number + 1)]
    p = 2

    while p * p <= n:

        # If prime[p] is not changed, then it is a prime
        if prime[p]:

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            print(p)


if __name__ == "__main__":
    n = 30
    print("Following are the prime numbers smaller")
    print("than or equal to", n)
    sieve_of_eratosthenes(n)
