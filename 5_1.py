n = int(input("введите количество цифр для вывода: "))
m = int(input("Введите первое число: "))
k = int(input("Введите второе число: "))
# numbers = [i for i in range(0,1000) if not i % m and i > k]
# numbers = list(numbers)
# print(numbers[:n])

i = k
count = 0
while count < n:
    if not i % m:
        count += 1
        print(i)
    i += 1
