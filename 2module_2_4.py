print('Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes =[]
primes = []
for num in numbers:
    if num != 1:
        for i in range(2, int(num // 2) + 1):
            if (num % i) == 0:
                not_primes.append(num)
                break
        else:
            is_primes = True
            primes.append(num)
            print(is_primes, num)
print("Primes: ", primes)
print("Not Primes: ", not_primes)

print('Конец работы по уроку "Цикл for. Элементы списка. Полезные функции в цикле"')
print("Created by VectorⓇ")

