name_test = ("Задача 1 - Работа со списками:")
print(name_test)
my_list =["инжир", "банан", "апельсин", "яблоко", "груша"]
print ("List:", my_list)
a = my_list [0::]
b = my_list [1::]
c = my_list [2::]
d = my_list [3::]
e = my_list [4::]
datas= (len(my_list))
print ("Всего", datas, "видов фруктов")
print ("First element:", my_list [0])
print ("First last:", my_list [4])
print("Sublist:",my_list[2],my_list[3], my_list[4] )
print("Modified Sublist:", c)
my_list[2] = "COCACOLA"
print("Modified list:",my_list)
print("Конец задачи:", name_test [11::])
print ("_____________________________")
# Конец задачи работа со списками
name_test = ("Задача 2 - Работа со словарями:")
print(name_test)
my_dict = {'Laptop': 'Ноутбук', 'Photo': 'Фотография', 'Apple':'Яблоко', 'Coconut': 'Кокос', 'Kids':'Ребенок'}
my_dict2 = {'Ноутбук':'Laptop',  'Фотография':'Photo', 'Яблоко':'Apple', 'Кокос':'Coconut', 'Ребенок':'Kids'}
print (type(my_dict))
print(my_dict)
print("В словаре всего",(len( my_dict )), "слов"), print(my_dict.keys())
dict = input('Для перевода на "RUS" введите слово из словаря, соблюдая регистр: ')
print("Слово", (dict),"переводится как -", my_dict.get(dict, "отсутсвует перевод в словаре"))
print (my_dict2.keys())
value = input('Для перевода на "US" введите слово на русском языке, соблюдая регистр:')
print("Слово", (value),"переводится как -", (my_dict2.get(value, "в словаре нет такого слова")))
update_key = input('Чтобы добавить новые слова в словарь введиет слово на АНГЛ. ')
update_value =input('Введите перевод: ')
my_dict.update({(update_key):(update_value)})
print(my_dict)
print("Спасибо теперь в словаре ",(len( my_dict )), "слов"), print(my_dict.keys())
#print(dict)
