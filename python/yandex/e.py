
def get_id_lists(cur_idx, max_lengths):

    res = []
    for i in range(len(cur_idx)):
        if cur_idx[i] < max_lengths[i]:
            res.append(i)

    return res


with open('input.txt', 'r') as file:
    input_lines = [line.strip() for line in file]

k = int(input_lines[0])

lst = []
if k <=0:
    pass
else:
    for i in range(1, k+1):
        numbers = [int(i) for i in input_lines[i].split(' ') if i]
        lst.append(numbers[1:])

    max_lengths = [len(i) for i in lst]

    result = []

    idx_lst = [0] * len(lst)
    id_lists = get_id_lists(idx_lst, max_lengths)

    while len(id_lists) >= 2:

        id_l = id_lists[0]
        min_val = lst[id_l][idx_lst[id_l]]

        for k in id_lists:
            v = lst[k]
            if v[idx_lst[k]] < min_val:
                min_val = v[idx_lst[k]]
                id_l = k

        idx_lst[id_l] += 1
        result.append(min_val)

        if idx_lst[id_l] < max_lengths[id_l]:
            next_n = lst[id_l][idx_lst[id_l]]
            while next_n == min_val:
                result.append(min_val)
                idx_lst[id_l] += 1

                if idx_lst[id_l] >= max_lengths[id_l]:
                    break
                next_n = lst[id_l][idx_lst[id_l]]

        if result[-1] == 100:
            break

        id_lists = get_id_lists(idx_lst, max_lengths)

    for i in range(len(idx_lst)):
        if idx_lst[i] < max_lengths[i]:
            result += lst[i][idx_lst[i]:]

    print(*result, sep=" ")
