sentence = input('Введите текст: ')
count_letters = {n: sentence.count(n) for n in sentence}
print(dict(count_letters))