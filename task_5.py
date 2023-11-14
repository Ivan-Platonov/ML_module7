print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль 
# среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

start, stop = ('',)*2
summ, count = 0, 0
def error_message():
  print('Необходимо ввести положительное число!!!')

while start == '':
  try:
    start = int(input('Введите первое число: '))
  except ValueError:
    error_message()

while stop == '':
  try:
    stop = int(input('Введите второе число: '))
  except ValueError:
    error_message()

if start > stop:
  start, stop = stop, start

for element in range(start, stop + 1):
  if element % 3 == 0:
    summ += element
    count += 1

summ = round(summ / count, 2)

print()
print(f'Среднее арифметическое всех чисел из отрезка [{start}; {stop}], включая крайние значения и которые кратны числу 3, равно: {summ}')
