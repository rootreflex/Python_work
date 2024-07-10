print ('"Задача "Съедобное, несъедобное":" ')


class Animal: # Класс животные
    def __init__(self, name):
        self.alive = True  # живое
        self.fed = False  # не накормлено
        self.name = name  # название животного

class Plant: # Класс растения
    def __init__(self, name, edible=False):
        self.edible = edible  # растение несъедобное
        self.name = name  # название растения

class Mammal(Animal): #Класс Млекопитающие
    def eat(self, food):  # метод eat для млекопитающих
        if isinstance(food, Plant):
            if food.edible:  # если растение съедобное
                print(f"{self.name} съел {food.name}")  # едим растение
                self.fed = True # наелся)
            else:
                print(f"{self.name} не стал есть {food.name}")  # нельзя есть не съедобное
                self.alive = False  # Умер

class Predator(Animal): # Класс Хищники
    def eat(self, food): # Метод
        if isinstance(food, Plant): # Проверяем, является ли еда растением
            if food.edible: # Если растение съедобное
                print(f"{self.name} съел {food.name}")  # Хищник съел растение
                self.fed = True  # Хищник накормлен
            else:
                print(f"{self.name} не стал есть {food.name}")  # Хищник отказался от еды
                self.alive = False  # Хищник погиб из-за несъедобного растения


class Flower(Plant): # Класс Цветы
    def __init__(self, name):
        super().__init__(name, edible=False)  # Цветы несъедобные

class Fruit(Plant): # Класс Фрукты
    def __init__(self, name):
        super().__init__(name, edible=True)  # Фрукты съедобные


a1 = Predator('Волк с Уолл-Стрит') # Хищник - 'Волк с Уолл-Стрит'
a2 = Mammal('Хатико') # Млекопитающее - 'Хатико'
a3 = Mammal('Слон')
p1 = Flower('Цветик семицветик') # Растение -'Цветик семицветик'
p2 = Fruit('Заводной апельсин') # Фрукт - 'Заводной апельсин'
p3 = Fruit('Банан')

# Вывод по разнообразию
print("Хищник: ", a1.name)  # Волк с Уолл-Стрит
print("Млекопитающее: ", a2.name)  # Хатико
print("Растение: ", p1.name)  # Цветик семицветик
print("Фрукт: ", p2.name)  # Заводной апельсин

print(f'{a1.name}', " - Живой?", a1.alive)
print(f'{a2.name}'," - Сытый?", a2.fed)
print(f'Пытаемся покормить {a1.name} - {p1.name}')
a1.eat(p1) # Хищник ест цветок
print(f'Пытаемся покормить {a2.name} - {p2.name}')
a2.eat(p2) # Млекопитающее ест фрукт

print(f'{a1.name}', " - Живой?", a1.alive)
print(f'{a2.name}'," - Наелся?", a2.fed)
print(f'Пытаемся покормить {a1.name} - {p2.name}')
a1.eat(p2) # Хищник есть фрукт
print(f'{a1.name}', " - Живой?", a1.alive)

print(f'Пытаемся покормить {a2.name} - {p1.name}')
a2.eat(p1) # млекопитающее ест цветок
print(f'Пытаемся покормить {a3.name} - {p3.name}')
a3.eat(p3) # Кормим слона
print(f'{a3.name}', " - Живой?", a3.alive)
print(f'{a3.name}'," - Наелся?", a3.fed)
a3.eat(p1)
print()
print()
print("Вывод по заданию")
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)