print('"Перегрузка операторов:"')
print("")

class Building:

    def __init__(self, numberOfFloors):
        self.buildingType = buildingType
        self.numberOfFloors = numberOfFloors
        self.say_info()  # Приветствие
        self.say_info2()
    def say_info(self):
        print(f'Наше здание имеет {self.numberOfFloors} этажей ')
    def say_info2(self):
        print(f'Мы рады сообщить об открытии филиала на {self.buildingType} этаже ')
    def __eq__(self, numberOfFloors):
        return (self.numberOfFloors == int(self.buildingType))
    def __lt__(self, numberOfFloors):
        return (self.numberOfFloors < int(self.buildingType))
    def __gt__(self, numberOfFloors):
        return (self.numberOfFloors > int(self.buildingType))

Vector = buildingType = ('11')
print("Убидимся что buildingType", type(buildingType))
Paradise = Building(25)
print(buildingType)
print(Paradise.numberOfFloors)
print('Наш филиал расположен выше 25го этажа?', Paradise < Vector)
print('Находится ли наш филиалл на 25ом этаже?', Paradise == Vector)
print('Находится ли наш филиалл ниже 25го этажа?', Paradise > Vector)



