def gen(
    cnt,
):
    m = (["("] * cnt) + ([")"] * cnt)

    print(*m, sep="")

    while True:
        idx = len(m) - 1
        cnt = 0

        while idx >= 0:
            if m[idx] == ")":
                cnt -= 1
            elif m[idx] == "(":
                cnt += 1

            if cnt < 0 and m[idx] == "(":
                break
            idx -= 1

        if idx < 0:
            break

        m[idx] = ")"

        v = (len(m) - idx + cnt) / 2 + idx
        for i in range(idx + 1, len(m)):
            if i <= v:
                m[i] = "("
            else:
                m[i] = ")"
        print(*m, sep="")


if __name__ == "__main__":

    import sys

    n = int(sys.stdin.readline().strip())
    gen(n)
