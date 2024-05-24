print('"Задача "Все ли равны?":"')
first = int(input("введите целое число: "))
print ("Вы ввели число ", first)
second = int(input("введите второе целое число: "))
print ("Вы ввели число ", second)
third = int(input("введите второе целое число: "))
print ("Вы ввели число ", third)
if first  == second and second  == third and third == first:
    print ("Вы ввели",3, "одинаковых числа")
elif first  == second or second  == third or third == first:
    print ("Вы ввели", 2, "одинаковых числа")

elif  first  != second or second  != third or third != first:
    print("Вы ввели" ,0, "одинаковых чисел")
