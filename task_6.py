print('Задача 6. Замечательные числа')

# Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.

# Пояснение:
# 15 -> 1*5*3 = 15 - получившееся число равно оригиналу, значит число надо вывести
# 16 -> 1*6*3 = 18 - число выводить не нужно, 18 не равно 16


print('Двузначные числа, которые равны утроенному произведению своих цифр: ')

for number in range(10, 99):
  if number == number // 10 * number % 10 * 3:
    print(number)
