print('"Задача" Нули ничто, отрицание недопустимо!')
while True:
    my_list_nul = [0]
    my_list = [-9, 42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    print("Длина заданногосписка", (len(my_list)), "цифр")
    print(my_list)

    if my_list[0] > my_list_nul[0]:
        my_list_nul.append(my_list[0])
        print(my_list[0])
    if len(my_list_nul) < 10:
        if my_list[1] > my_list_nul[0]:
            my_list_nul.append(my_list[1])
            print(my_list[1])
    if len(my_list_nul) < 10:
        if my_list[2] > my_list_nul[0]:
            my_list_nul.append(my_list[2])
            print(my_list[2])
    if len(my_list_nul) < 10:
        if my_list[3] > my_list_nul[0]:
            my_list_nul.append(my_list[3])
            print(my_list[3])
    if len(my_list_nul) < 10:
        if my_list[4] > my_list_nul[0]:
            my_list_nul.append(my_list[4])
            print(my_list[4])
    if len(my_list_nul) < 10:
        if my_list[5] > my_list_nul[0]:
            my_list_nul.append(my_list[5])
            print(my_list[5])
    if len(my_list_nul) < 10:
        if my_list[6] > my_list_nul[0]:
            my_list_nul.append(my_list[6])
            print(my_list[6])
    if len(my_list_nul) < 10:
        if my_list[7] > my_list_nul[0]:
            my_list_nul.append(my_list[7])
            print(my_list[7])
    if len(my_list_nul) < 10:
        if my_list[8] > my_list_nul[0]:
            my_list_nul.append(my_list[8])
            print(my_list[8])
    if len(my_list_nul) < 10:
        if my_list[9] > my_list_nul[0]:
            my_list_nul.append(my_list[9])
            print(my_list[9])
    if len(my_list_nul) < 10:
        if my_list[10] > my_list_nul[0]:
            my_list_nul.append(my_list[10])
            print(my_list[10])
    if len(my_list_nul) < 10:
        if my_list[11] > my_list_nul[0]:
            my_list_nul.append(my_list[11])
            print(my_list[11])
    if len(my_list_nul) < 10:
        if my_list[12] > my_list_nul[0]:
            my_list_nul.append(my_list[12])
            print(my_list[12])
    if len(my_list_nul) < 10:
        if my_list[13] > my_list_nul[0]:
            my_list_nul.append(my_list[13])
            print(my_list[13])
    break
print('КОНЕЦ - "Задача" Нули ничто, отрицание недопустимо!')
print('_________________________________________________________')


print('ВТОРОЙ ВАРИАНТ РЕШЕНИЯ - "Задача" Нули ничто, отрицание недопустимо!')

while True:
    my_list_nul = [0]
    my_list_2 = []
    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
    print("Длина заданногосписка", (len(my_list)), "цифр")
    print(my_list)
    num = 0
    my_list_2.append(my_list[num])
    if my_list[num] > my_list_nul[0]:
        print(my_list_2[num])
    for i in range(len(my_list)):
        num += 1
        if num < len(my_list):
            my_list_2.append(my_list[num])
            if my_list[num] > my_list_nul[0]:
                print(my_list_2[num])
    break

print('КОНЕЦ ВТОРОГА ВАРИАНТА - "Задача" Нули ничто, отрицание недопустимо!')
print(" ___________________________________________________________________")

print('САМЫЙ ПРОСТОЙ ВАРИАНТ - "Задача" Нули ничто, отрицание недопустимо!')


numbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

for number in numbers:
    if number > 0:
        print(number)

print('КОНЕЦ ПРОСТОГО ВАРИАНТА - "Задача" Нули ничто, отрицание недопустимо!')
print("Created by VectorⓇ")