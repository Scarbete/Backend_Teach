# 1 ) Выведите столбец четных чисел в промежутке о 0 до 20 (используйте цикл while)
# number = 0
# while not number == 20:
#     number += 1
#     print(number)

# 2 ) Программа запрашивает число и будет спрашивать до тех пор,
#     пока пользователь не введет отрицательное число.
#     Как только пользователь ввел отрицательное число,
#     программа завершает работу и в консоли выводит
#     сумму всех введенных положительных чисел. Например:
#     сперва я ввела 5, потом 7, следом -8, в консоли должно
#     появиться «сумма чисел - 12». Подсказка - используйте цикл while
# number0 = 0
# input_number = 0
# while input_number >= 0:
#     input_number = input(f"Введите число: ")
#     try:
#         input_number = int(input_number)
#         if input_number >= 0:
#             number0 += input_number
#         else:
#             break
#     except ValueError:
#         print("Введено не корректное значение")
#         break
# print(f"Вы ввели отрицательное число, сумма положительных составляет: ", number0)

# count = 0
#
# while True:
#     num = int(input('Введите число: '))
#
#     if num < 0:
#         break
#
#     count += num
#
# print(f'Сумма всех чисел: {count}')

# 3 ) Вывести все не четные числа от 1 до 20
# number = 0
# while number <= 19:
#     number += 1
#     if number % 2 == 1:
#         print(number)
#     else:
#         continue


# 4.1 ) Обратный отсчет от 10 до 1 нужно использовать цикл while и for
#
# for i in range(10, 0, -1):
#     print(i)


# 4.2)

i = 11
# while i<=11 and i>0:
while 11 >= i > 0:
    i -= 1
    print(i)