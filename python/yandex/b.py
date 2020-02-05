import sys

n = int(sys.stdin.readline().strip())

if n <= 0:
    print(0)
elif n > 10000:
    print(0)
else:

    bin_arr = []
    for i in range(n):
        bin_arr.append(sys.stdin.readline().strip())

    bin_str = "".join(bin_arr)

    parts = [i for i in bin_str.split('0') if i]

    if not parts:
        print(0)
    else:
        max_len_of_parts = len(parts[0])
        for i in range(1, len(parts)):
            part = parts[i]
            if len(part) > max_len_of_parts:
                max_len_of_parts = len(part)

        print(max_len_of_parts)
