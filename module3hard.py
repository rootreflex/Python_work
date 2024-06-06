
data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(args): # создаем функию для перебора видов параметров
    summ_ = 0 # начальное значение
    for i in args:
        if isinstance(i, list | tuple | set): # если тип лист тюпл  и множество
            summ_ += calculate_structure_sum(i) # суммируем
        elif isinstance(i, dict): # иначе это словарь
            for key in i: # перебираем ключи в словаре
                if isinstance(key, str): # если ключ str
                    summ_ += len(key) # складывваем длину ключей
                elif isinstance(key, int | float): # иначе ключ int или float
                    summ_ += key # сумируем ключи
            for j in i.values():   # создаем цикл j для перебора значений
                if isinstance(j, str): # если значение str
                    summ_ += len(j) # сумируем длину значений
                elif isinstance(j, int | float): # иначе int или float
                    summ_ += j #прибавляем их к int
        elif isinstance(i, int | float): # иначе  i является int | float
            summ_ += i # прибавляем к int
        elif isinstance(i, str): # иначе i str
            summ_ += len(i) # складываем длину str
    return summ_  # возвращаем к summ_
result = calculate_structure_sum(data_structure)
print(result) # выводим на печать)
