math_operation = input(
    'Выберите действие (1 : сложение, 2 : вычитание, 3 : умножение, 4 : деление, 5: возведение в степень, 6: извлечение квадратного корня)? Введите число от 1 до 6:  ')
while (int(math_operation) < 1 or int(math_operation) > 6) or not math_operation.isdigit():
    math_operation = input(
        'Выберите действие (1 : сложение, 2 : вычитание, 3 : умножение, 4 : деление, 5: возведение в степень, 6: извлечение квадратного корня)? Введите число от 1 до 6:  ')
first_digit = input('Введите число (число должно быть целым): ')
while not first_digit.isdigit():
    first_digit = input('Введите число (число должно быть целым): ')
if int(math_operation) == 6:
    print(int(first_digit) ** 0.5)
else:
    second_digit = input('Введите число 2 (число должно быть целым): ')
    while not second_digit.isdigit():
        second_digit = input('Введите число 2 (число должно быть целым): ')
    if int(math_operation) == 1:
        print(int(first_digit) + int(second_digit))
    elif int(math_operation) == 2:
        print(int(first_digit) - int(second_digit))
    elif int(math_operation) == 3:
        print(int(first_digit) * int(second_digit))
    elif int(math_operation) == 4:
        while int(second_digit) == 0:
            second_digit = input('Введите число 2 (число должно быть целым и отличным от нуля): ')
        while not second_digit.isdigit():
            second_digit = input('Введите число 2 (число должно быть целым и отличным от нуля): ')
        print(int(int(first_digit) / int(second_digit)))
    elif int(math_operation) == 5:
        print(int(first_digit) ** int(second_digit))
    elif int(math_operation) == 6:
        print(int(first_digit) ** 0.5)


