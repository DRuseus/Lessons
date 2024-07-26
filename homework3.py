# Решение задачи по уроку "Динамическая типизация"
name_ = 'Andrei'
print(f"Имя: {name_}", end='\nBозраст (int): ')
age_ = 24
print(age_, end='\nBозраст (float): ')
age_ = age_ + 1.25
print(age_, end='\nBозраст (str): ')
age_ = str(age_) + '1'
print(age_, end='\nЯвляется ли студентом (bool): ')
is_Student = True
print(is_Student, end='\nЯвляется ли студентом (str): ')
is_Student = 'True'
print(is_Student)
