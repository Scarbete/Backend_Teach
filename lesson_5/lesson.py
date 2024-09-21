# Структуру данных - Cловари ( dictionary )

# { 'name': 'Aesthetic' }

# { key: value }

# person = {
#    'name': 'Quasar',
#     1: 'Aesthetic',
#     False: 'Yanehz',
#     'hobby': ['Программирование', 'dwed'],
#     'married': True,
#     'famliy': {
#         'mother': 'mother',
#         'father': 'father'
#     }
# }
#
# print(person)
#
# print(person['name'])
#
# print(person['famliy']['mother'])
#
# person2 = dict(name='Quasar', age=20, isProgrammer=True)
#
# print(person2)

# zodiac = {
#     'taurus': 10 > 20 and 10 != 9 or 10 > 0
# }

student = {
    'name': 'Kutman',
    'age': 20,
    'hobby': ['Программирование', 'CODM', 'Music', 'Frontend', 'Backend'],
    'married': False,
    'did_he_receive_an_image_of_Afina\'s_feet': True
}

# print(student)
# CRUD

# READ

# print(student.keys())
# print(student.values())
# print(student.items())

# for keys, values in student.items():
#     print(keys)
#     print(values)


# CREATE
student['height'] = 180
# print(student)

student['hobby'].append('QA')
# print(student)

student.update({'new_name': 'Quasar'})
# print(student)

# UPDATE
student['name'] = 'Quasar'
# print(student)

student['hobby'][-1] = 'DevOps'
# print(student)

# DELETE
del student['new_name']
# print(student)

deleted_pop = student.pop('height')

# print(deleted_pop)
# print(student)

numbers = [i ** 5 for i in range(8, 20)]
print(numbers)

obj = {i: i * i for i in range(0, 10)}
print(obj)

new_obj = dict(enumerate('Quasar'))
print(new_obj)

test_dict = {
    'name': 'value'
}

test_set = {'Quasar', 20, True, False, True, 1, 0}
print(test_set)

plov = {'рис', 'морковь', 'лук', 'мясо'}
manty = {'тесто', 'лук', 'мясо'}

print(type(test_dict))
print(type(test_set))


