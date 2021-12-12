# квадратный корень - перебор
import math


def square_root(number):
    num_iterations = 0
    epicilon = 0.0001
    ans = 0.0

    while abs(pow(ans, 2) - number) >= epicilon:
        ans += 0.00001
        num_iterations += 1

    return "root = {}, iteration = {}".format(ans, num_iterations)


# квадратный корень - c применением бинарного поиска
def bsquare_root(number):
    num_iterations = 0
    epicilon = 0.0001
    low = 0.0
    high = number
    guess = (low + high) / 2
    while abs(pow(guess, 2) - number) >= epicilon:

        if pow(guess, 2) < number:
            low = guess
        else:
            high = guess

        guess = (low + high) / 2
        num_iterations += 1

    return "root = {}, iteration = {}".format(guess, num_iterations)


def root(A):
    # https://www.interviewbit.com/problems/square-root-of-integer/
    # Square root of an integer
    if A in (0, 1):
        return A

    start = 0
    end = A

    ans = None
    while start <= end:
        mid = (start + end) // 2

        if mid * mid == A:
            return mid

        if mid * mid > A:
            end = mid - 1
        else:
            start = mid + 1
            ans = mid

    return ans


if __name__ == "__main__":
    # print(square_root(123.45655))
    # print(bsquare_root(123.45655))
    assert root(16) == 4
    assert root(2) == 1
    assert root(0) == 0
    assert root(1) == 1
    assert root(3) == 1
    assert root(5) == 2
    assert root(6) == 2
    assert root(169078009) == 13003
