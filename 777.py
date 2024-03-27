# ПРОГРАММА УГАДАЙКА ЧИСЕЛ
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
# import random
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
# import random

# Функция проверки корректности введенных данных
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


# #*****************************************************************
# q = 1 # переменная для бесконечного цыкла while
# while q != 0:
#     from random import * # вызов модуля
#     number = randint(1, 100) # генерация рандомного числа по заданному диапазону
#
#     print('Добро пожаловать в числовую угадайку.', 'Введи число от 1 до 100 включительно, чтобы угадать число которое задумал компьютер. ')
#
#     def is_valid(x): # функция на проверку коректности вводимых данных
#      if x.isdigit() and 0 < int(x) < 101:
#          return True
#      else:
#          return False
#
#     count = 0
#     while True:
#         number_user = input()
#         if is_valid(number_user):
#             number_user = int(number_user)
#             count += 1
#         else:
#             print('А может быть все-таки введем целое число от 1 до 100?')
#             continue
#         if number_user > number:
#             print('Ваше число больше загаданного, попробуйте еще разок')
#         elif number_user < number:
#             print('Ваше число меньше загаданного, попробуйте еще разок')
#         else:
#             print('Вы угадали, поздравляем!')
#             break
#     print('Спасибо, что играли в числовую угадайку. Еще увидимся...''Вы отгадали с', +count, 'попытки.')
#
#     print('играть ещё ? / да / нет') # возможность продолжить или завершить игру
#     number_user_2 = input() # переменная по которой определяется дальнейшее выполнение цикла
#
#     ## переменная для бесконечного цыкла while
#     if number_user_2 == 'да':
#         q = 1 # переменная для бесконечного цыкла while
#         print('да')
#     else:
#         q = 0 # переменная для бесконечного цыкла while
#         print('Всего доброго')
#         print('Игра завершена ')
# #****************************************************************


# #****************************************************************
# #****************************************************************

# ПРОГРАММА МАГИЧЕСКИЙ ШАР 8

# Подключите модуль random;
# Создайте список answers, содержащий 20 потенциальных ответов (Бесспорно, Предрешено, и т.д.).
# Выведите текстовое сообщение: 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.';
# Уточните как зовут пользователя;
# Выведите слова приветствия, например, 'Привет Тимур'.
# Организуйте цикл, который будет запрашивать у пользователя данные;
# Запросите у пользователя вопрос;
# Выведите случайный ответ с помощью функции choice() передав список answers в качестве аргумента;
# Уточните у пользователя, хочет ли он задать еще один вопрос, если да, то вернитесь в основной цикл программы,
# если нет выведите сообщение 'Возвращайся если возникнут вопросы!' и завершите программу.

# import random # вызов модуля
# answers = ['Бесспорно', 'Мне кажется - да', 'Пока неясно, попробуй снова', 'Даже не думай',
#  'Предрешено',	'Вероятнее всего',	'Спроси позже',	'Мой ответ - нет',
# 'Никаких сомнений',	'Хорошие перспективы',	'Лучше не рассказывать', 'По моим данным - нет',
# 'Определённо да', 'Знаки говорят - да',	'Сейчас нельзя предсказать', 'Перспективы не очень хорошие',
# 'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
# name = input('Как тебя зовут ? :')
# print('Привет', name, 'я магический шар, и я знаю ответ на любой твой вопрос.')
# count = 0
# while count == 0:
#     answers_random = random.choice(answers) # генерирует случайный вывод из ранее созданного списка
#     print(input('Задай свой вопрос ! :'))
#     print(answers_random)
#     while count == 0:
#         n = (input('Ещё вопрос да ? или нет ?').lower())
#         if n == 'нет':
#             print('Возвращайся если возникнут вопросы!')
#             count += 1
#             break
#         elif n == 'да':
#             break
#         else:
#             print('Извини не понял ответа, сыграем ещё ? ')
# #****************************************************************
# #****************************************************************


# #****************************************************************
# #****************************************************************

#  ПРОГРАММА ГЕНЕРАТОР БЕЗОПАСНЫХ ПАРОЛЕЙ

# Подключите модуль random;
# Создайте строковые константы:
# Напишите функцию generate_password(), которая принимает два аргумента:
#
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
# Используя цикл for, сгенерируйте необходимое количество паролей.

# Заголовок программы
# Подключите модуль random;
# Создайте строковые константы:
# digits: 0123456789;
# lowercase_letters: abcdefghijklmnopqrstuvwxyz;
# uppercase_letters: ABCDEFGHIJKLMNOPQRSTUVWXYZ;
# punctuation: !#$%&*+-=?@^_.
# Создайте переменную chars = '', которая будет содержать все символы, которые могут быть в генерируемом пароле.


# Считывание пользовательских данных
# Программа должна запрашивать у пользователя следующую информацию:
#
# Количество паролей для генерации;
# Длину одного пароля;
# Включать ли цифры 0123456789?
# Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?
# Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?
# Включать ли символы !#$%&*+-=?@^_?
# Исключать ли неоднозначные символы il1Lo0O?


# Генерации пароля
# Напишите функцию generate_password(), которая принимает два аргумента:
#
# length: длину пароля;
# chars: алфавит из символов которого состоит пароль;
# и возвращает пароль.
#
# Используя цикл for, сгенерируйте необходимое количество паролей.

# #*******************************************

# # переменные на добавления в список символов через запрос о необходимости у пользователя # Заголовок программы
# digits = '0123456789'
# lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
# uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# punctuation = '!#$%&*+-=?@^_'
#
# ambiguous_characters = 'il1Lo0O' # неоднозначные символы
#
# chars = '' #  список символов
# s = '' #  переменная для перезаписи без неоднозначных символов
#
#
# #************************   генерируем список символов   (chars) Считывание пользовательских данных
# quantity = input('Количество паролей для генерации : ')
# if quantity.isdigit():
#     print('необходимое количество паролей зафиксировано', quantity)
# else:
#     print('Количество паролей для генерации, должно быть цыфрой')
#     quantity = input('Введите количество паролей для генерации в цыфрах : ')
# # print(quantity)
# length = input('Длину одного пароля : ') #
# if quantity.isdigit():
#     print('необходимая длинна одного пароля зафиксирована', length, 'символов')
# else:
#     print('длинна одного пароля для генерации, должна быть цыфрой')
#     length = input('Введите длину одного пароля : ')
# # print(long)
#
# numbers = (input('Включать ли цифры  ? да или нет : ').lower()) #
# if numbers == 'да':
#     chars += digits
#     print('цифры будут включены в пароль')
# else:
#     print('цифры НЕ будут включены в пароль')
#
# small_letter = (input('Включать ли строчные буквы ? да или нет : ').lower()) #
# if small_letter == 'да':
#     chars += lowercase_letters
#     print('строчные буквы будут включены в пароль')
# else:
#     print('строчные буквы НЕ будут включены в пароль')
#
# big_letter = (input('Включать ли прописные буквы ? да или нет : ').lower()) #
# if big_letter == 'да':
#     chars += uppercase_letters
#     print('прописные буквы будут включены в пароль')
# else:
#     print('прописные буквы НЕ будут включены в пароль')
#
# symbol = (input('Включать ли символы ? да или нет : ').lower()) #
# if symbol == 'да':
#     chars += punctuation
#     print('символы будут включены в пароль')
# else:
#     print('символы НЕ будут включены в пароль')
#
# symbol_ambiguous = (input('Исключать ли неоднозначные символы ? да или нет : ').lower()) #
# if symbol_ambiguous == 'да':
#     for i in range(len(chars)):
#         if not chars[i] in ambiguous_characters:
#             s += chars[i]
#     chars = s # перезаписали список символов , без неоднозначных символов .
#     print('неоднозначные символы будут исключены из пароля')
# if symbol_ambiguous != 'да':
#     print('неоднозначные символы НЕ будут исключены из пароля')
# #************************   сгенерировали список символов (chars)
#
# import random # вызов модуля
#
# def generate(): # функция по созданию пароля # Генерации пароля
#     password = ''
#     for _ in range(int(length)):
#         password += random.choice(chars) # выводит случайный элемент из строки и добовляет его в переменную
#     return password
#
#
# for _ in range(int(quantity)): # вызов функции нужно количество паролей # вывод паролей
#     print()
#     print(generate())
# #****************************************************************
# #****************************************************************


# #****************************************************************
# #***************************************************************
# ШИФР ЦЕЗАРЯ
# Описание проекта: требуется написать программу,
# способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
# Она должна запрашивать у пользователя следующие данные:
#
# направление: шифрование или дешифрование;
# язык алфавита: русский или английский;
# шаг сдвига (со сдвигом вправо).
# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
# Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять"
# при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".


# ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
# RU = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
# EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
#
#
# direction = input('ш or дш ? ') # шифрование или дешифрование;
# language = input('ру or ен ? ') # язык
#
# step = int(input('Введи число от 0 до 32 , на которое нужно сдвинуть текст ')) # шаг сдвига он же ключ для дешифрования
#
# text = input('Введите текст который нужно зашифровать' )
# y = ''
# x = ''
#
# if direction == 'ш' and language == 'ру' and 0 < step < 32:
#     for i in range(len(text)):
#         for q in range(len(ru)):
#             if text[i].isalpha(): # с функцией для проверки текста на состав
#                 # (правда если число состоит только из буквенных символов)
#                 if text[i] == ru[q]:
#                     y += ru[q + step]
#                     break
#                 elif text[i] == RU[q]:
#                     y += ' ' + RU[q + step]
#                     break
#             else:
#                 y += text[i]
#                 break
# elif direction != 'ш' and language != 'ру' and 0 > step or step > 32:
#     print('Введенны некоректные данные, повторите запрос')
# print(y.lstrip()) # вывод c применениев функции по убиранию пробела в начале текста
#
#
# # Верхний код шифрование ру
# # НИЖНИК КОД ДЕШИФРОВАНИЕ ру
#
# if direction == 'дш' and language == 'ру' and 0 < step < 32:
#     for i in range(len(text)):
#         for q in range(len(ru)):
#             if text[i].isalpha():  # с функцией для проверки текста на состав
#             # (правда если число состоит только из буквенных символов)
#                 if text[i] == ru[q]:
#                     x += ru[q - step]
#                     break
#                 elif text[i] == RU[q]:
#                     x += ' ' + RU[q - step]
#                     break
#             else:
#                 x += text[i]
#                 break
#     print(x.lstrip())
#
# #==========================================================================
#
# if direction == 'ш' and language == 'ен' and 0 < step < 26:
#     for i in range(len(text)):
#         for q in range(len(en)):
#             if text[i].isalpha(): # с функцией для проверки текста на состав
#                 # (правда если число состоит только из буквенных символов)
#                 if text[i] == en[q]:
#                     y += en[q + step]
#                     break
#                 elif text[i] == EN[q]:
#                     y += ' ' + EN[q + step]
#                     break
#             else:
#                 y += text[i]
#                 break
# elif direction != 'ш' and language != 'ру' and 0 > step or step > 32:
#     print('Введенны некоректные данные, повторите запрос')
# print(y.lstrip()) # вывод c применениев функции по убиранию пробела в начале текста
#
# # Верхний код шифрование ен
# # НИЖНИК КОД ДЕШИФРОВАНИЕ ен
#
# if direction == 'дш' and language == 'ен' and 0 < step < 26:
#     for i in range(len(text)):
#         for q in range(len(en)):
#             if text[i].isalpha():  # с функцией для проверки текста на состав
#             # (правда если число состоит только из буквенных символов)
#                 if text[i] == en[q]:
#                     x += en[q - step]
#                     break
#                 elif text[i] == EN[q]:
#                     x += ' ' + EN[q - step]
#                     break
#             else:
#                 x += text[i]
#                 break
#     print(x.lstrip())
#
#
#
# #==============================================================
# #==============================================================
# #==============================================================
# На вход программе подается строка текста на английском языке,
# в которой нужно зашифровать все слова.
# Каждое слово строки следует зашифровать с помощью шифра Цезаря
# (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными,
# а прописные – прописными. Гарантируется,
# что между различными словами присутствует один пробел.
# EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
# en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
# s = input()
# s1 = s.split()
# x = ''
# t = ''
# b = [] # длина здвига
# for i in range(len(s)):
#     if s[i].isalpha():
#         x += 'a'
#     else:
#         x += ' '
# y = x.split() # СОЛИЧЕСТВО КАЖДОГО СЛОВА
# for i in range(len(y)):
#     c = len(y[i])
#     b.append(c)
#
# for i in range(len(s1)): # КОЛИЧЕСТВО СЛОВ В СПИСКЕ
#     c = s1[i] + ' '
#     p = b[i] # длина слова
#     for r in range(len(c)):
#         for q in range(len(en)): # КОЛИЧЕСТВО АЛФАВИТА
#             if c[r].isalpha():
#                 if en[q] == c[r]:
#                     t += en[q + p]
#                     break
#                 elif EN[q] == c[r]:
#                     t += EN[q + p]
#                     break
#             else:
#                 t += c[r]
#                 break
# print(t)
# #=============================================================
# #=============================================================
# #=============================================================


# Калькулятор систем счисления ? ПЕРЕВОДА ЧИСЛА В ДЕСЯТИЧНУЮ СИСТЕМУ СЧЕСЛЕНИЯ
# s_1 = input('Для перевода в десятичную систему счисления,введите числа через пробел! : ')
# q = int(input('Из какой системы счисления нужно перевести ? :  '))
#
# s_2 = s_1.split()
# s = []
# for i in range(len(s_2)):
#     s.append(int(s_2[i]))
# s.reverse()
# #     88 32 22 16 17
# x = 0
# for i in range(len(s)):
#      x += s[i]*q**i
# print(x)


# #=============================================================
# #=============================================================
# #=============================================================
# x = int(input()) # На вход программе подается натуральное число в десятичной системе счисления.
#
# x_2 = bin(x) # переводит число в двоичную
# print(int(x_2[2::])) # выводит число (без приставки)
#
# x_1 = oct(x) # переводит число в восьмеричную
# print(int(x_1[2::])) # выводит число (без приставки)
#
# x_3 = hex(x) # переводит число в шестнадцатеричную
# print(x_3[2::].upper()) # выводит число (без приставки) в ВЕРХНЕМ регистре
# #=============================================================
# #=============================================================
# #=============================================================


# Угадайка слов


# Заголовок программы
# Подключите модуль random;
# Создайте глобальный список word_list,
# содержащий слова, которые будут использоваться в игре.
name = input('Привет, как тебя зовут ?  Вод : ')
print('Будем знакомы', name, 'меня называют угадайка слов :)')
user_2 = input('ты готов-ва сыграть ?  Вод : ').upper()
while user_2 != 'НЕТ':
    import random

    word_list = ['Авокадо', 'Артишок', 'Баклажан', 'Батат', 'Брокколи', 'Брюква',
                 'Горох', 'Дайкон', 'Кабачок', 'Каперсы', 'Капуста', 'Картофель',
                 'Кукуруза', 'Лук', 'Морковь', 'Огурец', 'Патиссон',
                 'Перец', 'Редис', 'Редька', 'Репа', 'Свекла', 'Сельдерей',
                 'Спаржа', 'Помидор', 'Тыква', 'Фасоль', 'Хрен', 'Цуккини',
                 'Чеснок']


    #  случайное слово из списка word_list в верхнем регистре.
    def get_word():
        word = random.randint(0, len(word_list))
        return word_list[word].upper()


    #  случайное слово из списка word_list в верхнем регистре.

    q = get_word()

    u = q[0]

    tries = 0


    # функция получения текущего состояния
    def display_hangman(tries):
        stages = [
            '''


                             O
                            \\|/
                             |
                            / \\

                       ''',
            '''


                             O
                            \\|/
                             |
                            / 
            Я не хотел бы больше терять свои части как Джавани
            по этому лови подсказку, загаданное слово является овощем !
            И начинается на букву ''' + q[0],

            '''


                             O
                            \\|/
                             |


                    ''',
            '''


                             O
                            \\|
                             |



                    ''',
            '''


                             O
                             |
                             |


                    ''',
            '''


                             O
                             |



                    ''',
            '''


                             O




                    ''',
            '''


                      УВЫ ИГРА ОКОНЧИНА
                    если хочеш сыграть ещё отправь да 
                    или нет для завершения игры. 




                    ''',
        ]
        return stages[tries]


    # функция получения текущего состояния

    y = display_hangman(tries)

    print('Добро пожаловать в угадайку слов!, меня сделал Саша и Настя')
    print('Загаданное мной слово состоит из', ('_ ' * len(q)), len(q),
          'букв')  # строка, содержащая символы _ на каждую букву задуманного слова
    print('Ты можешь допустить всего 7 не правельных ответов')
    # word_completion = ''
    d = []
    f = '_ ' * len(q)
    f = f.split()


    def play():
        print(y)
        print(*f)


    print(play())

    guessed_letters = [' ']  # список уже названных букв
    guessed = False  # сигнальная метка
    count = 0
    # while guessed != True:
    while tries != 7:
        user = input('Введи букву : ')
        user = user.upper()
        # print(q)
        x = q.split
        print(q)

        if user in guessed_letters:
            print('уже было')
            continue
        elif user in q:
            print('Отлично, такая буква есть')
            for i in range(len(q)):
                if user == q[i]:
                    del f[i]
                    f.insert(i, user)
        else:
            # убираем части человечка
            print('Такой буквы нет в загаданом слове')
            tries += 1
            y = display_hangman(tries)
        play()
        # убираем части человечка

        guessed_letters.append(user)  # список уже названных букв

    user_2 = input('Вод : ').upper()

print('Всего доброго')

# import random
#
# word_list = ['Авокадо', 'Артишок','Баклажан', 'Батат', 'Брокколи', 'Брюква',
#              'Горох', 'Дайкон','Кабачок', 'Каперсы', 'Капуста', 'Картофель',
#              'Кукуруза', 'Лук', 'Морковь',  'Огурец',  'Патиссон',
#              'Перец', 'Редис', 'Редька', 'Репа', 'Свекла', 'Сельдерей',
#              'Спаржа', 'Помидор', 'Тыква', 'Фасоль', 'Хрен', 'Цуккини',
#              'Чеснок']
#
# #  случайное слово из списка word_list в верхнем регистре.
# def get_word():
#     word = random.randint(0, len(word_list))
#     return word_list[word].upper()
# #  случайное слово из списка word_list в верхнем регистре.
#
#
# q = get_word()
#
# tries = 0
#
# # функция получения текущего состояния
# def display_hangman(tries):
#     stages = [
#         '''
#
#
#                          O
#                         \\|/
#                          |
#                         / \\
#
#                    ''',
#         '''
#
#
#                          O
#                         \\|/
#                          |
#                         /
#
#                 ''',
#
#         '''
#
#
#                          O
#                         \\|/
#                          |
#
#
#                 ''',
#         '''
#
#
#                          O
#                         \\|
#                          |
#
#
#                 ''',
#         '''
#
#
#                          O
#                          |
#                          |
#
#
#                 ''',
#         '''
#
#
#                          O
#                          |
#
#
#
#                 ''',
#         '''
#
#
#                          O
#
#
#
#
#                 ''',
#         '''
#
#
#                   УВЫ ИГРА ОКОНЧИНА
#                 человечек закончился
#                 если хочеш сыграть ещё отправь да
#                 или нет для завершения игры.
#
#
#
#
#                 ''',
#     ]
#     return stages[tries]
# # функция получения текущего состояния
#
# y = display_hangman(tries)
#
# print('Добро пожаловать в угадайку слов!, меня сделал Саша и Настя')
# print('Загаданное мной слово состоит из', ('_ ' * len(q)), len(q), 'букв')  # строка, содержащая символы _ на каждую букву задуманного слова
# print('Ты можешь допустить всего 7 не правельных ответов')
# # word_completion = ''
# d = []
# f = '_ ' * len(q)
# f = f.split()
#
# def play():
#     print(y)
#     print(*f)
#
# print(play())
#
#
# guessed_letters = [' ']               # список уже названных букв
# guessed = False # сигнальная метка
# count = 0
# # while guessed != True:
# while tries != 7:
#     user = input('Введи букву : ')
#     user = user.upper()
#     # print(q)
#     x = q.split
#     print(q)
#     if user in guessed_letters:
#         print('уже было')
#         continue
#     elif user in q:
#         print('Отлично, такая буква есть')
#         for i in range(len(q)):
#             if user == q[i]:
#                 del f[i]
#                 f.insert(i, user)
#     else:
#     #убираем части человечка
#         print('Такой буквы нет в загаданом слове')
#         tries += 1
#         y = display_hangman(tries)
#     play()
#     # убираем части человечка
#
#     guessed_letters.append(user)  # список уже названных букв
#проверка