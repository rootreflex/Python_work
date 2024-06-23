print('"Различие атрибутов класса и экземпляра:"')
print("")

from random import choice, randint
class Buiding:
    total = 0
    def __init__(self, name='Объект'):
        self.name = name
        self.quantity = randint(1, 50)
        self.buildingType = choice(['Ноутбук', 'Телефон', 'Фотоаппарат', 'Телевизор', 'Принтер','Умная колонка', 'Видеокамера', 'Ксерокс', 'Монитор', 'Компьютер'])
        Buiding.total +=1
    def __str__(self):
        list_ = list(map(lambda x, y: '\t' + str(x) + ' = ' + str(y) + '\n', self.__dict__.keys(),
                         self.__dict__.values()))
        return f'\nНазвание объекта "{self.name}":\n' + ' '.join(list_)

buid_list = [Buiding('Объект №'+str(i)) for i in range(1, 41)]

print(*buid_list)
print('Всего объектов:', Buiding.total)