def kwadraten_som(grondgetallen):
    'returns de som van de kwadraten van alle positieve getallen.'
    y = 0
    for x in grondgetallen:
        if x > 0:
            y = y + x**2
    return (y)

lst = [4, 5, 3, -81]
print(kwadraten_som(lst))