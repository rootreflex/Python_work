
print ('"Практическое задание по теме: "Словари" ')
my_dict = {}
name = {'Victor'}
print ("Тип имени", (type(name)))
name = list(name)
year = 1984
print ("Тип даты рождения", (type(year)))
my_dict.update({(name[0]):(year)})
name2 = {'Valentin','Boris'}
name2 =list(name2)
year = 2000, 2003
#print(name2[0])
#print(year[0])
my_dict.update({(name2[0]):(year[0]),(name2[1]):(year[1])})
print ("Тип словаря", type(my_dict))
print ("В словаре такие имена: ",my_dict.keys())

dict = input('Введите любое имя, не из словаря: ')
print ("В словаре нет имени: ", (dict), my_dict.get(dict, "ИЗВИНИТЕ"))
dict = input('Введите любое имя , из словаря: ')
print ("Имя: ", (dict), my_dict.get(dict, "В словаре нет такого имени"),"года рождения.")
# a=my_dict.pop(name2[0])
# print(a)
print ("Значение из словаря для 'Victor'", my_dict.get('Victor'))
print("Удаляем Victor из словаря", my_dict.pop('Victor'))
print(my_dict)

print ('"Конец задяния "СЛОВАРИ "')
print ('_____________________________________________________')
print("ЗАДАНИЕ МНОЖЕСТВА")

my_set = {1,1,1,1,2,2,2,2,3,4,5,5,5,"Babana", True}
print("Наше множество", my_set)
list_2 =(my_set)
list_2= set(list_2)
print("Превращаем множество в список_1: ", list_2)
list_ = [3,3,3,3,5,5,5,5,8,8,8,9,9,9,4,4,]
print("Создаем новый список_2: ",list_)
my_set.add(6)
print("Просто захотелось добавить по среди задания цифру (6 :)", my_set)
list_= set(list_)

print("Превращаем новый список_2 в множество",list_)

print("Добавляем к новому множеству цифру ( 7 )",list_.add(7))
print(list_)
print("Удаляем из нового множества цифру( 3 )", list_.discard(3))
print(list_)
list_=set(list_)

my_tuple = (3.5, 2.3, 4)
print("создаем tuple", my_tuple)

my_set.add(my_tuple)
print("добавляем tuple в наш наше первое множество ", my_set)


print("КОНЕЦ ЗАДАНИЯ МНОЖЕСТВА")


print("Created by VectorⓇ")