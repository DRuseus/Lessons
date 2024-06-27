import random

seed = random.randint(3, 20)    # seed == Число от 3 до 20, которое появляется в первом поле.
second_space = []
print(f'\033[31mЧисло в первом поле:\033[0m {seed}')

# Создаём массив от 1 до числа, которое выпало в первом поле головоломки -1
def set_num_list(seed_of_trap):
    s_list = []
    for i in range(seed_of_trap - 1):
        s_list.append(i + 1)
    return s_list


seed_list = set_num_list(seed)


# Функция вычисления пароля
def operation(s_list=seed_list):
    global second_space
    global seed
    for oneN in s_list:
        for twoN in s_list:
            if oneN == twoN or oneN > twoN:
                continue
            if seed % (oneN + twoN) == 0:
                second_space.append(oneN)
                second_space.append(twoN)
                continue
    return second_space


print('\033[31mПароль для второго поля: \033[0m', *operation(seed_list), sep='')
