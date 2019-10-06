
def winner(erica, bob):
    e_score = 0
    b_score = 0
    for e, b, in zip(erica, bob):
        e_score += get_score_by_symbol(e)
        b_score += get_score_by_symbol(b)

    if e_score == b_score:
        return 'Tie'
    elif e_score > b_score:
        return 'Erica'
    else:
        return 'Bob'


def get_score_by_symbol(s: str):
    if s == 'E':
        return 1
    elif s == 'M':
        return 3
    elif s == 'H':
        return 5
    else:
        raise Exception


print(winner("EHH", "EME"))
print(winner("E", "H"))
print(winner("H", "H"))