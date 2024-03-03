from random import *
number = randint(1, 100)
number_user = bool
print('Попробуй отгадать число в диапазоне от 1 до 5 включительно :')
while number != number_user:
    number_user = int(input())
    if number_user > number:
        print('Слишком много, попробуйте еще раз')
    elif number_user < number:
        print('Слишком мало, попробуйте еще раз')
print('Вы угадали, поздравляем!')