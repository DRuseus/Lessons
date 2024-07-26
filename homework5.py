# Решение практического задания по уроку "Неизменяемые и изменяемые объекты. Кортежи"
immutable_var = (1, 2.5, '3', False, 5, -4.5j, b'2', [35, 28])
print(immutable_var[7], immutable_var[2::2])
print(immutable_var, '\n')

a_ = immutable_var * 2
b_ = a_ + (1234567890, 987654321)
print(a_, '\n', b_, '\n', sep='')
# Конкатенация и "умножение" (не помню, как операция точно называется) - единственные операции изменения "tuple()"

# immutable_var[1] = 2.7
# print(immutable_var)
# Кортеж "immutable_var" не может быть изменён, так как он является неизменяемым типом данных "tuble".
# Невозможность изменить переменные внутри кортежа связана с тем, что этот тип данных оптимизирован для уменьшения веса и функция изменения увеличила бы занимаемое место в ОЗУ.

# Далее идёт изменение типа данных list
mutable_list = [1, 2.5, '3', True, 5, -4.5j, b'3', (35, 28)]
print(mutable_list)
mutable_list[7] = (28, 33)
mutable_list.append(+1.23j)
mutable_list = mutable_list + list(immutable_var)
mutable_list.remove(mutable_list[5])
mutable_list[3] = False
i = len(mutable_list)
while i < 20:
    mutable_list.append(i)
    i = len(mutable_list)
print(mutable_list)

