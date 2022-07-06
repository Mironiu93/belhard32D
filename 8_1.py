def PascalTriangle(raws):
    raw = [1]
    for i in range(raws):
        print(raw)
        raw = [sum(x) for x in zip([0] + raw, raw + [0])]


PascalTriangle(20)