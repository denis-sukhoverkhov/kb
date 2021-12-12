if __name__ == "__main__":
    # anagram
    import sys

    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()

    if sorted(str1) == sorted(str2):
        print(1)
    else:
        print(0)
