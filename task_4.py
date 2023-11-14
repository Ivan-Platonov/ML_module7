print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

student_count = ''
count_3, count_4, count_5 = (0,)*3
def error_message():
  print('Необходимо ввести положительное число, не равное нулю!!!')
  
while student_count == '':
  try:
    student_count = int(input('Введите количество учеников в классе: '))
    if student_count <= 0:
      error_message()
      student_count = ''
  except ValueError:
    error_message()

for i in range(student_count):
  mark = ''
  while mark == '':
    try:
      mark = int(input(f'Введите оценку ученика {i + 1}: '))
      if mark != 3 and mark != 4 and mark != 5:
        print('Оценка сегодня может быть 3, 4 или 5')
        mark = ''
    except ValueError:
      error_message()
  if mark == 3:
    count_3 +=1
  elif mark == 4:
    count_4 +=1
  elif mark == 5:
    count_5 +=1

print()
if count_3 > count_4 and count_3 > count_5:
  print('Сегодня больше троечников')
elif count_4 > count_3 and count_4 > count_5:
  print('Сегодня больше хорошистов')
elif count_5 > count_3 and count_5 > count_4:
  print('Сегодня больше отличников')
elif count_3 == count_4 and count_3 > count_5:
  print('Сегодня больше троечников и хорошистов')
elif count_3 == count_5 and count_3 > count_4:
  print('Сегодня больше троечников и отличников')
elif count_4 == count_5 and count_4 > count_3:
  print('Сегодня больше хорошистов и отличников')
else:
  print('Сегодня одинаковое количество учеников с разной успеваемостью')
    