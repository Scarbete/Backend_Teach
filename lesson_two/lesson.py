# условные конструкции ( if, elif, else )
# ( ==, <=, >=, !=, <>, and, or, not )
# bool - логический тип данных ( True, False )
# True - правда
# False - ложь
# +=, -=, /=, *=, **=, //=
# len(), isinstans()
# [start:stop:step]
# isalpha - метод строки который проверяет не состоит только из букв
# isnumeric - не состоит из цифр

# 1, "good", True, 10 > 5 - True
# 0, None, -3 - False

# print('10 > 5: ', type(10 > 5))

# is_married = False
#
# if not is_married:
#     print('ok')
# else:
#     print('not ok')

# word = 'word'
# print(len(word))

# is_married = True
#
# if isinstance(is_married, int):
#     print('ok')
# else:
#     print('not ok')

# name = 'Quasar'

# phone1 = '+996-550-50-90-80'
# phone2 = '+007-550-50-90-80'
# phone3 = '+008-550-50-90-80'
#
# country_code = phone1[0:4]
#
# if country_code == '+996':
#     print('Это номер КР')

# password = input('Введите пароль: ')
#
# if len(password) >= 8 and not password.isalpha() and not password.isnumeric():
#     print('good')
# else:
#     print('bad')

# print(len('10'))

# obj = {
#     'name': 'Quasar',
#     'age': 20
# }
#
# print(len(obj))

# try:
#     age = int(input('Введите возраст: '))
#     print(type(age))
# except ValueError and TypeError:
#     print('Ошибка типа данных')
#
#
# try:
#     age = int(input('Введите возраст: '))
#     print(type(age))
# except ValueError:
#     print('Ошибка ValueError')
# except TypeError:
#     print('Ошибка TypeError')
# finally:
#     print('finally')

# def int_input(placeholder: str) -> int:
#     input_one = input(placeholder)
#
#     try:
#         input_one = int(input_one)
#     except ValueError:
#         print('Не корректное значение')
#         return 0
#
#     return input_one
#
#
# while True:
#     number = int_input(placeholder=f'Введите размерность списка: ')
#     array_one = []
#     element = 0
#
#     for elements in range(number):
#         print()
# from typing import List
#
#
# arr = [10, 15, 20, 25, 30]
#
#
# def plus_5(enter_arr: List[int]):
#     """
#     как работает......
#     """
#     new_arr = []
#
#     for number in enter_arr:
#         new_arr.append(number + 5)
#
#     return new_arr
#
#
# updated_arr = plus_5(enter_arr=arr)
# print(updated_arr)
# print(plus_5.__doc__)
# print(input.__doc__)

def int_input(placeholder: str) -> int:

    while True:
        input_one = input(placeholder)

        try:
            input_one = int(input_one)
        except ValueError:
            print('Не корректное значение...')

        if isinstance(input_one, int):
            return input_one

num = int_input('Введите значение: ')
