n = int(input('Введите число n: '))
data = {i: {"name": input("name: "), "email": input("email: ")} for i in range(n)}
print(data)