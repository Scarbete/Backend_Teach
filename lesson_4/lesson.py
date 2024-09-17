# Список ( Массив ) - Array ( list )
# Кортежи ( Tuple )
# CRUD - операции над List
# C - create
# R - read
# U - update
# D - delete
# Срезы

# Read
# toys = ['Мишка', 'Мячик', 'Машинка', 20, 23.3232, True, False]
# numbers = list(range(1, 21))
# new_numbers = [num ** 2 for num in numbers]

# print(numbers)
# print(new_numbers)

# print(toys)
# print(toys[0])
# print(toys[-1])
# print(toys[1][1])

# CRUD

# Create
# toys.append('Вертолетик')
# toys.append('Шарики')
# toys.append(['Красный', 'Синий'])
# print('append', toys)

# toys.insert(0, 'Quasar')
# toys.insert(-1, 'Aesthetic')
# print('insert', toys)

# Delete
# toys.remove('Машинка')
# print('remove', toys)

# del toys[1]
# print('remove', toys)

# deleted_obj = toys.pop(1)
# print('deleted_obj', deleted_obj)
# print('pop', toys)

# Update
# toys[2] = 'Мяч'
# print('update', toys)

# vertolet = toys.pop(1)
# toys.insert(2, vertolet)

# toys.insert(2, toys.pop(1))

# print('change', toys)

# arr_toys = ['Мишка', 'Мячик', 'Машинка']
# tuple_1 = ('Мишка', 'Мячик', 'Машинка')
# tuple_2 = tuple(['Мишка', 'Мячик', 'Машинка'])
# tuple_3 = 'Мишка', 'Мячик', 'Машинка'

# tuple_1 += ('good', 'bad')
# arr_toys += ['good', 'bad']
# print(tuple_1)
# print(arr_toys)

# print(type(tuple_1))
# print(type(tuple_2))
# print(type(tuple_3))

# arr1 = ['Мишка', 'Мячик', 'Машинка']
# arr2 = ['Мишка', 'Мячик', 'Машинка']
# arr2 = arr1
# arr2 = list(arr1)
#
# arr2.append('bad')
#
# print('arr1', arr1)
# print('arr2', arr2)
#
# print(id(arr1))
# print(id(arr2))
#
# if arr1 == arr2:
#     print('ok')
# else:
#     print('bad')

toys = ['Мишка', 'Мячик', 'Машинка', 20, 23.3232, True, False]

tuple_toys = tuple(toys)
tuple_toys2 = (toys, 2)
print(tuple_toys)
print(tuple_toys2)
print(type(tuple_toys))
print(type(tuple_toys2))

# for i in range(0, 11):
#     print(i)

# new_arr = list(toys)
#
# for i in new_arr:
#     print(i)
#
#     if i == 'Машинка':
#         new_arr[new_arr.index(i)] = 'Changed!'
#
# print(new_arr)
