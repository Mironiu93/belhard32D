# multiply = lambda a, b: a*b
# print(multiply(4, 5))
# numbers = ["1", "2", "3"]
# numbers = tuple(map(lambda x: int(x) ** 2, numbers))
# print(numbers)

# lst = [3, 45, 45, 23, 2345,664, 9, 93, 95,49]
# res = list(filter(lambda x: not x % 3, lst))
# print(res)
# print(lst)

def foo(a: int, b: list = []) -> list:
    if b is None:
        b = []
    b.append(a)
    return b
print(foo(5))
print(foo(4))

numbers = [1, 2, 3, 4, [5, 6, [7,8,9,[3,2,3,]]]]

def multipy(numbers: list) -> int:
    counter = 1
    for number in numbers:
        if isinstance(number, int):
            counter += number
        else:
            counter += multiply(number)
    return counter
