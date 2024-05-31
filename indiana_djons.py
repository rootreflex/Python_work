print('"Indiana Jones":')

import random

def door_lock():
    password =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    row = random.choice(password[2:])
    return row
row = door_lock()
print("каменная вставка имеет число: ", row) # Создал рандомное число

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
door_key = []
door_key_2 = []
door_key_3 =[]
for a in list_a:
    for b in list_a:
        if (a + b) == row:
            # print(a, b)
            door_key.append(a), door_key.append(b)
            print(door_key)
for c in list_a:
    if (row % c) == 0:
        door_key_2.append(c)
        print("Делитель", c)
        print(door_key_2)
for a in list_a:
    for b in list_a:
        if (a + b) == door_key_2:
            print(a, b)
            door_key_3.append(a), door_key_3.append(b)
            print(door_key_3)



print('"Indiana Jones":')
print("Created by VectorⓇ")