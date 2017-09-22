def negatives(n):
    'prints the negative numbers of a list.'
    for x in n:
        if x < 0:
            print(x)

negatives([4, 0, -1, -3, 6, -9])