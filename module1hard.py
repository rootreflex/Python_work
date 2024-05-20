grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# print("тип оценок", (type(grades)))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students2 = list(students)# Преобразуем студентов в список
# print(len( grades ))

# Создаем функцию, которая будет сортировать список в алфавитном порядке:
def sortByAlphabet(students2):
        return students2[0] # Ключом является первый символ в каждой строке, сортируем по нему
# Вторая функция, сортирующая список по длине строки:

print ('Список студентов: ', students) # >>> ['a', 'cc', 'bbb']
students2.sort(key=sortByAlphabet) # Каждый элемент массива передается в качестве параметра функции
print ('Список студентов в алфавитном порядке: ', students2) # >>> ['a', 'bbb', 'cc']

numbers = (grades)
#print (type(numbers))
average = sum (grades[0]) / len (grades[0]),sum (grades[1]) / len (grades[1]),sum (grades[2]) / len (grades[2]),sum (grades[3]) / len (grades[3]),sum (grades[4]) / len (grades[4])
average2 = len (average)
print ("В группе всего", average2 , "студентов")
#print("Средний бал каждого ученика по алфавиту", (average))
print (students2)
my_students_dict = {}
my_students_dict.update({(students2[0]):(average[0]), (students2[1]):(average[1]), (students2[2]):(average[2]), (students2[3]):(average[3]),(students2[4]):(average[4])})
#print(my_students_dict)
dict = input('Введите имя студента чтобы узнать его средний балл: ')
print("Студент: ", (dict),"средний балл: ", my_students_dict.get(dict, "У ВАС НЕТ ТАКОГО СТУДЕНТА"))
# print (my_students_dict.keys())
update_key = input('Чтобы добавить нового студента, ВВЕДИТЕ ИМЯ СТУДЕНТА:  ')
update_value = input ('Введите средний балл студента: ')
# print(update_value)
# print(type(update_value))
my_students_dict.update({(update_key):(update_value)})
# print(grades)
print(my_students_dict)
# grades = (my_students_dict.values())
print(update_value)
print("Спасибо теперь в группе ",(len( my_students_dict )), "студентов"), print(my_students_dict.keys())
print(my_students_dict)