first_digit = input('Введите число 1 (число должно быть целым): ')
while not first_digit.isdigit():
    first_digit = input('Введите число 1 (число должно быть целым): ')
second_digit = input('Введите число 2 (число должно быть целым): ')
while not second_digit.isdigit():
    second_digit = input('Введите число 2 (число должно быть целым): ')
math_operation = input('Какое действие произвести с числом (1 : сложить, 2 : отнять, 3 : умножить, 4 :разделить, 5: возвести в степень)? Введите число от 1 до 5:  ')
while not math_operation.isdigit():
     math_operation = input('Какое действие произвести с числом (1 : сложить, 2 : отнять, 3 : умножить, 4 :разделить, 5: возвести в степень)? Введите число от 1 до 5:  ')
while int(math_operation) < 1 or int(math_operation) > 5:
    math_operation = input(
        'Какое действие произвести с числом (1 : сложить, 2 : отнять, 3 : умножить, 4 :разделить, 5: возвести в степень)? Введите число от 1 до 5:  ')
if int(math_operation) == 1:
    print(int(first_digit) + int(second_digit))
elif int(math_operation) == 2:
    print(int(first_digit) - int(second_digit))
elif int(math_operation) == 3:
    print(int(first_digit) * int(second_digit))
elif int(math_operation) == 4:
    print(int(first_digit) / int(second_digit))
elif int(math_operation) == 5:
    print(int(first_digit) ** int(second_digit))
else:
    print('Введено не корректное действие')

