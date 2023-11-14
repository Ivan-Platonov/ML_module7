print('Задача 2. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.

salary_summ = 0
for i in range(12):
  salary = ''
  while salary == '':
    try:
      salary = float(input(f'Введите свою зарплату за {i + 1}-й месяц: '))
    except ValueError:
      print('Необходимо ввести положительное число!!!')
  salary_summ += round(salary/12, 2)
print()
print(f'Средняя зарплата за год составляет: {salary_summ} рублей')