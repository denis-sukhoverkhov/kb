def fountainActivation(a):
    coverage_list = []
    len_of_garden = len(a)

    for i in range(0, len(a)):
        idx = i + 1
        from_v, to_v = max([idx - a[i], 1]), min([idx + a[i], len_of_garden])
        # length = to_v - from_v
        coverage_list.append((from_v, to_v))

    ct_fountans = []

    # uncovered_borders = (1, len_of_garden)
    for i in range(len_of_garden):
        from_v = coverage_list[i][0]
        to_v = coverage_list[i][1]
        summ_fountans = 1

        if from_v == 1 and to_v == len_of_garden:
            ct_fountans.append(summ_fountans)
            continue

        for j in range(i+1, len_of_garden):
            ft = coverage_list[j]
            if from_v > ft[0] >= 1:
                from_v = ft[0]
                to_v = ft[1] if ft[1] > to_v else to_v
                summ_fountans += 1
            elif ft[1] > to_v and to_v < len_of_garden:
                to_v = ft[1]
                summ_fountans += 1

            if from_v == 1 and to_v == len_of_garden:
                ct_fountans.append(summ_fountans)
                break

    return min(ct_fountans)


print(fountainActivation([1, 1, 1]))