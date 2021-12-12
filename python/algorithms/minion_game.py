def minion_game(string):
    vowels = ["A", "E", "I", "O", "U"]
    kevsc, stusc = 0, 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevsc += len(s) - i
        else:
            stusc += len(s) - i

    if kevsc > stusc:
        print(f"Kevin {kevsc}")
    elif kevsc < stusc:
        print(f"Stuart {stusc}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
