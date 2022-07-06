def asc(a):
    b = []
    l = len(a)
    for i in range(l):
        x = min(a)
        b.append(x)
        a.remove(x)
    return b
print (asc([2, 5, 8, 7, 44, 54, 23]))