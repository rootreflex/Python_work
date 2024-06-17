
print('"Специальные методы классов:"')
print("")
import webbrowser

class House:
    def __init__(self, name, numberOfFloors):
        self.name = name
        self.numberOfFloors = numberOfFloors
        self.say_info()  # Приветствие
    def say_info(self):
        print(f'Добро пожаловать в наш {self.name} сервис расположен на {self.numberOfFloors} этаже ') # До метода set
    def set_name(self, New_name):
        self.name = New_name
    def set_numberOfFloors(self, floors):
        self.numberOfFloors = floors
        self.say_info2()  # Переезд!
    def say_info2(self):
        print(f'Мы рады сообщить что {self.name} переехал на {self.numberOfFloors} этаж ') # После метода set


person = House("Vector_service", 0)

print(person.name)
print(person.numberOfFloors)

person.set_name("Vector_service")
person.set_numberOfFloors(25)


print(person.name)
print(person.numberOfFloors)

class Info:
    def __init__(self, name):
        self.name = name
        self.say_info3()
    def say_info3(self):
        print(f'Подробней о услугах {self.name} можно ознакомиться на нашем сайте')

detales = Info("Vector_service")
webbrowser.open_new("https://sc-vector.com")
url = "https://sc-vector.com"
print(url)

print("")
print("")
print("Created by VectorⓇ")
