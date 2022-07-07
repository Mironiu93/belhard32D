# str_list = [1, 2, 3, [4, 5,6], 7, [8, 9], 10, 11, [12, 13, [14, 15, 16]]]
# what_to_do = input('Какой элемент списка показать? Введите знак > или <: ')
# count = [0]
# if str_list == '>':
#     count += 1
#      if count == [-1]:
#         print(count[0])
#     print(count)
# elif str_list == '<':
#     count -= 1
#     if count == [0]:
#          print[:-1]
#     print(count)
# else:
#     print('Введен неверный символ. Пожалуйста, повторите попытку.')

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def pagination(numbers: list[int]):
    print(numbers[0])
    i = 0
    while True:
        direction: str = input('direction: ')
        if direction == '>':
            i += 1
            if i == len(numbers):
                i = 0
            print(numbers[i])
        if direction == '<':
            i -= 1
            if i == len(numbers) - 1:
                i = -1
            print(numbers[i])
    return numbers[i]