print('"Indiana Jones":')
print("")

import random # импортируем random

n = list(range(3, 21))  # Заданый список от 3 до 20.
x = random.choice(n)    # выбираем рандомное число.
y = ""                  # создаем список для сохранения нашей пары.
for i in range(x): # перебираем число x от 0 до x.
    for j in range(x): # перебираем второе число для сложения с x
        if x % ((i+1) + (j+1)) == 0 and j > i: # x % (i+j) == 0 и j>i
            y = y + str(i+1) + str(j+1) # сохраняем в y

print("каменная вставка имеет число: \n", x  ,"\nсекретный ключ: \n", y)
print("")
print("")
print('"Indiana Jones":')
print("Created by VectorⓇ")