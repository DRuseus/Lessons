# Решение №1 практического задания по модулю №1 "Базовые структуры данных." (Решение подслушано в ТГ канале
students = {'Вася Васильев', 'Петя Петров', 'Иван Иванов', 'Рома Романов', 'Коля Николаев'}
grades = [[4,2,2,4,5], [1,2,2,3,3], [4,5,5,3,4], [5,3,4,4,4,], [3,2,2,2,2]]
dict_of_stud = dict()
grades[0] = sum(grades[0])/len(grades[0])
grades[1] = sum(grades[1])/len(grades[1])
grades[2] = sum(grades[2])/len(grades[2])
grades[3] = sum(grades[3])/len(grades[3])
grades[4] = sum(grades[4])/len(grades[4])
students_ = list(students)
students_.sort()
dict_of_stud = zip(students_, grades)
dict_of_stud = dict(dict_of_stud)
print(dict_of_stud)


# Решение №2 практического задания по модулю №1 "Базовые структуры данных." (как я бы сделал до того, как глянул подсказку в ТГ канале)

# Создание списка из имён учеников
students_1 = input('Введите мена учеников учеников через запятую: ').split(',')
grades_1 = list([0]) * len(students_1)
dict_of_stud_1 = dict()
x = 0
# В этом цикле происходит перебор учеников по отдельности для рукописного присвоения им оценок индивидуально для каждого
for i in students_1:
    grades_1[x] = input(f'Введитте оценки ученика через пробел {students_1[x]}: ').split()
    a = 0
    # В этом цикле происходит перевод списка оценок, который получается при вводе для каждого ученика, из строкового типа данных в целочисленный тип данных
    for i in grades_1[x]:
        grades_1[x][a] = int(grades_1[x][a])
        a += 1
    grades_1[x] = sum(grades_1[x])/len(grades_1[x])
    x += 1

dict_of_stud_1 = dict(zip(students_1, grades_1))
# Я тут воспользовался подсмотренным оператором zip(), но на свмом деле опять перебрал бы всё цыклом через присвоение как сделано выше^^^

print(dict_of_stud_1)