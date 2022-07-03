import requests


def solution(url, port, a, b):
    params = {
        'a': a,
        'b': b,
    }
    result = requests.get(f"{url}:{port}", params=params)

    numbers = result.json()

    numbers.sort()

    return numbers


if __name__ == "__main__":
    with open("input.txt", "r") as fi:
        url = fi.readline().strip()
        port = fi.readline().strip()
        a = fi.readline().strip()
        b = fi.readline().strip()

    numbers = solution(url, port, a, b)

    with open("output.txt", "w") as fo:
        for n in numbers:
            fo.write(f"{n}\n")
