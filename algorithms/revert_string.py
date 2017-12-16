
# 1) Перевернуть строчку
my_str = "i am programmer"
new_str = my_str[::-1]
print(new_str)

# алгоритмически
i = 0
j = len(my_str) - 1
while i <= j:
    print(my_str)
    i_ = my_str[i]
    j_ = my_str[j]
    sl1 = my_str[:i]
    sl2 = my_str[i+1:j]
    sl3 = my_str[j+1:]

    my_str = sl1 + j_ + sl2 + i_ + sl3
    i += 1
    j -= 1
