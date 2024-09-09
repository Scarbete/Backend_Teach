# Циклы ( for & while )

# language = 'Python'

# for word in language:
#     print(word)

# for number in range(1, 11):
#     print(number)

# i - iterable, item

# [1234567890]

# for i in range(10):
#     print(i)

# print(word[0])
# print(word[1])
# print(word[2])
# print(word[3])
# print(word[4])
# print(word[5])

# language = 'Python'

# for i in language:
#     if i == 'h':
#         break
#     print(i)

# for i in language:
#     if i == 'h':
#         continue
#     print(i)

# if True:
#     print('ok')

# i = 0

# while i < 10:
#     print('i: ', i)
#     i += 1

# while True:
#     text = input('Enter stop sycle or not ( yes ): ')
#
#     if text == 'yes':
#         break
#
#     i += 1
#     print(i)

# rus = 'йцукенгшщзхъфывапролджэячсмитьбю.'
# eng = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./'
#
# while True:
#     text = input('\nВведите слово: ')
#
#     for letter in text:
#         if letter in rus:
#             print(eng[rus.index(letter)], end='')
#         else:
#             print(rus[eng.index(letter)], end='')

# name = 'Quasar'
#
# if 'Q' in name:
#     print('ok')
# else:
#     print('not ok')

# list - массив, список

# fruits = ['яблоко', 'банан (yanehz)', 'черешня']
#
# arr = ['яблоко', 123, 123.123, True, False]
#
# print(fruits)
# print(type(fruits))
# print(len(arr))
#
# for i in arr:
#     print(f'item: {i}')

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# print(matrix[-1][-1])
#
# print(matrix[len(matrix) - 1][len(matrix[len(matrix) - 1]) - 1])

# for row in matrix:
#     print(f'row: {row}')
#
#     for num in row:
#         print(f'num in row: {num}')


