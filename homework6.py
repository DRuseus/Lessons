# Решение практического задания по теме "Словари и множества"
my_dict = {'Abdula': 11, 'Magamed': 23, 'Jafar': 7, 'Amir': 1, 'Hafali': 3, 'Killreal': 15.5}
my_dict['Amir'] = 41
print(my_dict)

# Вывод значения по существующему ключу
print(my_dict['Jafar'])
# Вывод значения по несуществующему ключу (без ошибки)
print(my_dict.get('Kirill'))

# Добавление двух пар того же формата
my_dict.update({'Pasani': True,
                'Vache_rebyata': False})
# Удаление пары
del my_dict['Killreal']
print(my_dict, '\n')


# Работа с множествами
my_set = {1, 3, 7, 7, False, 13, 37, 21, 21, 7, 13, 1, True}   # Почему "True" не отображается в выводе???
print(my_set)

# Добавление двух элементов в множество
my_set.update({19, 17})
# Удаление элемента из множества
my_set.remove(False)
my_set.discard(22)
print(my_set)

# TEST!!! It's testing change