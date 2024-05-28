print('Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"')

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
not_primes =[]
primes = []
for num in numbers[1:]:
    for i in range(2, int(num // 2) + 1):
        if (num % i) == 0:
            break
    else:
        primes.append(num)
    not_primes = [num for num in numbers[1:] if num not in primes]
print("Primes: ", primes)
# как ни крутил, цифра 1 всеравно попадает в Primes, пока срезал ее из списка таким образом [1:].
print("Not Primes: ", not_primes)
# либо могу срезать из списка при печати) print("Primes: ", primes[1:])
print('Конец работы по уроку "Цикл for. Элементы списка. Полезные функции в цикле"')
print("Created by VectorⓇ")