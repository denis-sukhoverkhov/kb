# камни и украшения
import sys

if __name__ == "__main__":
    j = sys.stdin.readline().strip()
    s = sys.stdin.readline().strip()

    summ = 0
    for i in s:
        if i in j:
            summ += 1

    print(summ)
