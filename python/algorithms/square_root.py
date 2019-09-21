# квадратный корень - перебор
def square_root(number):
    num_iterations = 0
    epicilon = 0.0001
    ans = 0.0

    while abs(pow(ans, 2) - number) >= epicilon:
        ans += 0.00001
        num_iterations += 1

    return 'root = {}, iteration = {}'.format(ans, num_iterations)


print(square_root(123.45655))


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

    return 'root = {}, iteration = {}'.format(guess, num_iterations)


print(bsquare_root(123.45655))
