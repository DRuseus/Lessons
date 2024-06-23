# Решение задачи №1 по уроку "Условная конструкция. Операторы if, elif, else."
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
else:
    print('0')


# Решение задачи №1 по уроку "Условная конструкция. Операторы if, elif, else." (так бы я никогда не делал)
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and second == third:
    print('3')
elif first == second or second == third or first == third:
    print('2')
elif not first == second and not second == third:
    print('0')


# Решение задачи №1 по уроку "Условная конструкция. Операторы if, elif, else."

