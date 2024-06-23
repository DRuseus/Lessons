# Решение задачи №1 по уроку "Стиль кода часть II. Цикл While."
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
end = len(my_list)
result_list = []
while end > num:
    if my_list[num] > 0:
        result_list.append(my_list[num])
        num += 1
    else:
        num += 1
        continue
    if num == end:
        break
print(f'Конец цикла. Результат: {result_list}')

# Решение задачи №2 по уроку "Стиль кода часть II. Цикл While."
# (Тут ничего особо не поменялось, просто в условии цикла я заранее определил количество циклов функцией range().)
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0
result_list = []
while range(end):
    if my_list[num] > 0:
        result_list.append(my_list[num])
        num += 1
    else:
        num += 1
        continue
    if num == end:
        break
print(f'Конец цикла. Результат: {result_list}')

# Просто так
my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
result_list = []
for num in my_list:
    if num > 0:
        result_list.append(num)
result_list.sort(reverse=True)  # Ревёрснул тоже просто так
print(f'Конец цикла. Результат: {result_list}')
