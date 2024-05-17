name_test = ("Задача 1 - Задайте переменные разных типов данных: кортеж")
print(name_test)
immutable_var = 11, 24, 53, True, "Vector"
print(immutable_var)

name_test = ("Задача 2 - Создание изменяемых структур данных: список")
print(name_test)
mutable_list = [54, 789, 123, "Hello", ("Привет")]
print(mutable_list)
mutable_list[3] = "Goodby"
mutable_list[4] = "Пока"
print(mutable_list)
mutable_list .extend(["Доброе утро"])
print (mutable_list [4] .upper())
#конец задачи "Создание изменяемых структур данных: список"
print ("_____________________________")