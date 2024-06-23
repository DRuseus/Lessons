# Решение задачи по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = []
primes = []
not_primes = []

# Здесь просто создаётся массив от 1 до произвольного числа
inp_var = int(input('\033[0;0;31mВведите число, до которого хотите составить список простых чисел:\033[0;0;0m '))
i = 1
while i in range(inp_var + 1):
    numbers.append(i)
    i += 1
print(f'List of numbers out of {i - 1}: {numbers}')

primes = []
not_primes = []

# Процесс отсеивания простых от сложных чисел
for num in numbers[1:]:
    for n in numbers[1:num]:
        if num % n == 0 and num != n:
            not_primes.append(num)
            break
        elif num % n == 0 and num == n:
            primes.append(num)

# Посчитал количество простых и сложных чисел в выбранном диапазоне (из любопытства)
len_primes = len(primes)
len_not_primes = len(not_primes)

print(f'Primes numbers is {len_primes}: {primes}.\nNot Primes numbers is {len_not_primes}: {not_primes}.')
