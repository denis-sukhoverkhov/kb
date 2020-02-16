

def merge_lists():
    count = {str(i): 0 for i in range(101)}

    with open('input.txt', 'r') as file:
        for line in file:
            start = line.find(' ')
            if start > 0:
                for i in line[start + 1:].split(' '):
                    count[i.strip()] += 1

    # for idx, val in enumerate(count):
    #     print(*([idx] * val), sep=" ")

    for i in range(101):
        print(*([i]*count[str(i)]), sep=" ")


if __name__ == '__main__':
    merge_lists()
