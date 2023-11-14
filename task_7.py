print('Задача 7. Пропавшая карточка')

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

# Пример:
# Введите количество карточек: 5
# Введите номер оставшейся карточки: 1
# Введите номер оставшейся карточки: 4
# Введите номер оставшейся карточки: 5
# Введите номер оставшейся карточки: 3

# Номер пропавшей карточки: 2

cards_quantity, card_number = '', ''
cards_number_summ, cards_number_summ_fact = 0, 0

#Для себя добавил проверку ввода повторного гомера карточек
history_cards_number = []                                    #Для себя

def error_message():
  print('Необходимо ввести число больше 2!!!')

while cards_quantity == '':
  try:
    cards_quantity = int(input('Введите количество карточек: '))
    if cards_quantity <= 2:
      error_message()
      cards_quantity = ''
  except ValueError:
    error_message()

for card in range(cards_quantity + 1):
  cards_number_summ += card

for card in range(cards_quantity - 1):
  card_number = ''
  while card_number == '':
    try:
      card_number = int(input('Введите номер оставшейся карточки: '))
      if card_number > cards_quantity:                     
        print('Нельзя превышать количество карточек!!!')     
        card_number = ''
        
      elif card_number in history_cards_number:              #Для себя
        print('Вы уже ввели этот номер!!!')                  #Для себя
        card_number = ''                                     #Для себя
      else:                                                  #Для себя
        history_cards_number.append(card_number)             #Для себя
        
        cards_number_summ_fact += card_number
    except ValueError:
      print('Необходимо ввести число!!!')

print('Номер пропавшей карточки:', cards_number_summ - cards_number_summ_fact)
