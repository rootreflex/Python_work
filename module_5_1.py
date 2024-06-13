print('"Атрибуты и методы объекта":')
print("")

from random import randint as rn
class House:
    def __init__(self, name, number_of_floor):
        global new_floor
        self.name = name # Название
        self.number_of_floors = number_of_floor # Этажность
        self.say_info() # Приветствие
    def say_info(self):
        global number_of_floors
        print(f'Добро пожаловать в наш {self.name}, здание имеет {self.number_of_floors} этажей')
    def go_to(self, new_floor):
        global number_of_floors
        self.new_floor = new_floor
        if new_floor > self.number_of_floors:
            print(f'В знании {self.name}, Такого этажа не существует')
        elif new_floor == 0:
            print(f'В знании {self.name}, Такого этажа не существует')
        else:
            print(f'Благодарим Вас что выбрали : {self.name}, вы приехали на  {new_floor} этаж')


h1 = House('ЖК Горский', 11)
h2 = House('Домик в деревне',3)
new_floor = rn(0,20)
print(h1.name, h1.number_of_floors)
print(h2.name, h2.number_of_floors)
print('Лифт вызван на', new_floor, 'этаж' )

h1.go_to(new_floor)
h2.go_to(new_floor)

print("")
print("")
print("Created by VectorⓇ")