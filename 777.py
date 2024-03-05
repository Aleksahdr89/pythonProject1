# Угадайка чисел
#
# Описание проекта:
# программа генерирует случайное число в диапазоне от 1 до 100
# и просит пользователя угадать это число.
# Если догадка пользователя больше случайного числа,
# то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'.
# Если догадка меньше случайного числа,
# то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'.
# Если пользователь угадывает число,
# то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
#
# from random import *
# number = randint(1, 100)
# number_user = bool
# print('Добро пожаловать в числовую угадайку')
# while number != number_user:
#     print('Веди число')
#     number_user = int(input())
#     if number_user > number:
#         print('Слишком много, попробуйте еще раз')
#     elif number_user < number:
#         print('Слишком мало, попробуйте еще раз')
# print('Вы угадали, поздравляем!')
#





# Заголовок программы
#
# 1) Подключите модуль random;
# 2) Сгенерируйте случайное число от 1до 100;
# Выведите текст приветствия пользователю:
# 'Добро пожаловать в числовую угадайку'.
#
# from random import *
# number = randint(1, 100)
# print('Добро пожаловать в числовую угадайку')
#





#Функция проверки корректности введенных данных
#
# Напишите функцию is_valid() в которую передается один строковый аргумент.
# Функция возвращает значение True если переданный аргумент является целым числом от 1 до 100
# и False в противном случае.
#
# from random import *
# number = randint(1, 100)
# number_user = input()
# def is_valid(x):
#      if x.isdigit() and 0 < int(x) < 101:
#          return True
#      else:
#          return False
# print(is_valid(number_user))
#




# Основной цикл программы
#
# 1) Организуйте цикл, который будет запрашивать у пользователя данные =
# (цикл может быть бесконечным (while True) или может использовать сигнальную метку с последующим переключением,
# после угадывания числа);
# 2) Запросите у пользователя число от 1 до 100;
# 3) Проверьте введенные данные с помощью функции is_valid()
#
# ---если данные некорректны, выведите текст: 'А может быть все-таки введем целое число от 1 до 100?'
# и перейдите к следующей итерации основного цикла;
# ---если данные корректны, преобразуйте их к целому числу для удобства дальнейшей работы.
#


#****************************************************************
q = 1 # переменная для бесконечного цыкла while
while q != 0:
    from random import * # вызов модуля
    number = randint(1, 100) # генерация рандомного числа по заданному диапазону

    print('Добро пожаловать в числовую угадайку.', 'Веди число от 1 до 100 включительно. ')

    def is_valid(x): # функция на проверку коректности вводимых данных
     if x.isdigit() and 0 < int(x) < 101:
         return True
     else:
         return False

    count = 0
    while True:
        number_user = input()
        if is_valid(number_user):
            number_user = int(number_user)
            count += 1
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if number_user > number:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif number_user < number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...''Вы отгадали с', +count, 'попытки.')

    print('играть ещё ? / да / нет') # возможность продолжить или завершить игру
    number_user_2 = input() # переменная по которой определяется дальнейшее выполнение цикла

    ## переменная для бесконечного цыкла while
    if number_user_2 == 'да':
        q = 1 # переменная для бесконечного цыкла while
        print('да')
    else:
        q = 0 # переменная для бесконечного цыкла while
        print('Всего доброго')
        print('Игра завершена ')
#****************************************************************