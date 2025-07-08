def calc(a):
    return a - 0


records = [1, 40, 95]

calcul = [calc(a) for a in records]

calculation = map(calc, records)


# alternative with lambda

calcul_l = [(lambda a: a - 0)(a) for a in records]

calculation_l = list(map(lambda a: a - 0, records))
